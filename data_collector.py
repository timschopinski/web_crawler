from typing import List
import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, PageElement
from page import Page
from urls.url import Url


class DataCollector:

    def __init__(self):
        self._urls = []
        self.data: List[Page] = []

    @staticmethod
    def _get_soup(url: Url) -> BeautifulSoup:
        soup = None
        try:
            r = requests.get(url.to_string(), allow_redirects=False, timeout=5)
            soup = BeautifulSoup(r.content, 'html.parser')
        except Exception as e:
            print(e)
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

    def _collect_data(self, base_url: Url, parent_url: Url, depth: int, max_depth: int):
        soup = self._get_soup(parent_url)
        if soup is None:
            return
        subpage_tags = self._get_subpage_tags(soup)
        title = self._get_title(soup)

        self._urls.append(parent_url.to_string())
        new_page = Page(parent_url, base_url, title, subpage_tags)
        self.data.append(new_page)

        depth += 1
        for subpage_url in new_page.subpages_urls:
            if subpage_url.to_string() and depth < max_depth and subpage_url.to_string() not in self._urls:
                print(subpage_url.to_string())
                self._collect_data(base_url, subpage_url, depth, max_depth)

    def _count_references(self):
        for page in self.data:
            for child_url in page.get_unique_subpages_urls():
                for p in self.data:
                    if p.url == child_url:
                        p.reference_count += 1

    def get_page_data(self, base_url: Url, max_depth: int = 2) -> List[Page]:
        
        self._collect_data(base_url, base_url, 0, max_depth)
        self._count_references()
        return self.data
