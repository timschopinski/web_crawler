import copy
from typing import List
import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, PageElement
from page import Page
from urls.url import Url
import asyncio
import aiohttp
from time import perf_counter


class DataCollector:

    def __init__(self):
        self._urls = []
        self.data: List[Page] = []
        self.soups = {}

    @staticmethod
    async def _get_soup(url: Url):
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(url.to_string(), allow_redirects=False, ssl=False) as resp:
                body = await resp.text()
                soup = BeautifulSoup(body, 'html.parser')
                #
                # soup = None
                # try:
                #     r = requests.get(url.to_string(), allow_redirects=False, timeout=5)
                #     soup = BeautifulSoup(r.content, 'html.parser')
                # except Exception as e:
                #     print(e)
                print(url.to_string())

                # self.soups.update({url: soup})
                return soup

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

    # async def _collect_data(self, base_url: Url, parent_url: Url, depth: int, max_depth: int):
    #     print('test')
    #     soup = await self._get_soup(parent_url)
    #
    #     if soup is None:
    #         return
    #     subpage_tags = self._get_subpage_tags(soup)
    #     title = self._get_title(soup)
    #
    #     self._urls.append(parent_url.to_string())
    #     new_page = Page(parent_url, base_url, title, subpage_tags)
    #     self.data.append(new_page)
    #
    #     depth += 1
    #
    #     tasks = []
    #     for subpage_url in new_page.subpages_urls:
    #         if subpage_url.to_string() and depth < max_depth and subpage_url.to_string() not in self._urls:
    #             print(subpage_url.to_string())
    #             # self._collect_data(base_url, subpage_url, depth, max_depth)
    #             task = asyncio.create_task(self._collect_data(base_url, subpage_url, depth, max_depth))
    #             tasks.append(task)
    #     await asyncio.gather(*tasks)
    #

    async def _collect_data(self, base_url: Url, parent_url: Url, depth: int, max_depth: int):
        soup = await self._get_soup(parent_url)

        if soup is None:
            return
        subpage_tags = self._get_subpage_tags(soup)
        title = self._get_title(soup)

        self._urls.append(parent_url.to_string())
        new_page = Page(parent_url, base_url, title, subpage_tags)
        self.data.append(new_page)

        depth += 1

        tasks = []
        for subpage_url in new_page.subpages_urls:
            if subpage_url.to_string() and depth < max_depth and subpage_url.to_string() not in self._urls:
                print(subpage_url.to_string())
                # self._collect_data(base_url, subpage_url, depth, max_depth)
                task = asyncio.create_task(self._collect_data(base_url, subpage_url, depth, max_depth))
                tasks.append(task)
        await asyncio.gather(*tasks)

    def _count_references(self):
        for page in self.data:
            for child_url in page.get_unique_subpages_urls():
                for p in self.data:
                    if p.url == child_url:
                        p.reference_count += 1

    async def get_page_data(self, base_url: Url, max_depth: int = 2) -> List[Page]:
        t1 = perf_counter()

        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(self._collect_data(base_url, base_url, 0, max_depth))

        await self._collect_data(base_url, base_url, 0, max_depth)

        # await self._get_soup(base_url)
        # print(self.soups)
        # await self._collect_data(base_url, base_url, 0, max_depth, self.soups[base_url])
        #
        # self._collect_data(base_url, base_url, 0, max_depth)

        t2 = perf_counter()
        print(t2-t1)
        self._count_references()
        return self.data
