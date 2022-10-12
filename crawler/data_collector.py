from typing import List
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup
from bs4.element import ResultSet, PageElement
from logger.logger import Logger
from urls.page import Page
from urls.url import Url
import asyncio
from asyncio.tasks import Task
from management.argument_manager import ArgumentManager
import aiohttp


class DataCollector:

    def __init__(self):
        self._urls: List[Url] = []
        self.data: List[Page] = []
        self.allow_redirects = False
        self.timeout = 10

    async def _get_soup(self, url: Url) -> BeautifulSoup:
        print(url.to_string())
        try:
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get(url.to_string(), allow_redirects=self.allow_redirects, ssl=False, timeout=ClientTimeout(total=self.timeout)) as resp:
                    body = await resp.text()
                    soup = BeautifulSoup(body, 'html.parser')
                    return soup
        except asyncio.exceptions.TimeoutError as e:
            Logger.log_timout_error()

    @staticmethod
    def _get_subpage_tags(soup: BeautifulSoup) -> ResultSet[PageElement]:
        return soup.find_all('a', href=True)

    @staticmethod
    def _get_title(soup: BeautifulSoup) -> str:
        try:
            title = soup.find('title').text
        except AttributeError:
            title = ''
        return title

    async def _collect_data(self, base_url: Url, parent_url: Url, depth: int, max_depth: int) -> None:
        soup = await self._get_soup(parent_url)

        if soup is None:
            return
        subpage_tags = self._get_subpage_tags(soup)
        title = self._get_title(soup)

        self._urls.append(parent_url)
        new_page = Page(parent_url, base_url, title, subpage_tags)
        self.data.append(new_page)

        depth += 1

        tasks: List[Task] = []
        for subpage_url in new_page.subpages_urls:
            if subpage_url.to_string() and depth < max_depth and subpage_url not in self._urls:
                task = asyncio.create_task(self._collect_data(base_url, subpage_url, depth, max_depth))
                tasks.append(task)
        await asyncio.gather(*tasks)

    def _count_references(self) -> None:
        for page in self.data:
            for child_url in page.get_unique_subpages_urls():
                for p in self.data:
                    if p.url == child_url:
                        p.reference_count += 1

    async def get_page_data(self, argument_manager: ArgumentManager) -> List[Page]:
        max_depth = argument_manager.max_depth
        base_url = argument_manager.page
        self.timeout = argument_manager.timeout
        self.allow_redirects = argument_manager.allow_redirects
        await self._collect_data(base_url, base_url, 0, max_depth)
        self._count_references()
        return self.data
