from typing import List

from bs4.element import PageElement, ResultSet
from urls.url import Url
from urls.subpage_url import SubpageUrl


class Page:

    def __init__(self, url: Url, base_url: Url, title: str, subpage_tags: ResultSet[PageElement]):
        self.url = url.to_string()
        self.title = title
        self.subpages_urls = [SubpageUrl(base_url, tag) for tag in subpage_tags]
        self._number_of_internal_links = self._count_internal_links(subpage_tags)
        self._number_of_external_links = self._count_external_links(subpage_tags)
        self.reference_count = 0

    @staticmethod
    def is_external_link(link: PageElement) -> bool:
        return 'http' in link

    def get_unique_subpages_urls(self) -> List[str]:
        return list(dict.fromkeys([url.to_string() for url in self.subpages_urls]))

    def _count_external_links(self, subpage_tags: ResultSet[PageElement]) -> int:
        return len([link for link in subpage_tags if self.is_external_link(link['href'])])

    def _count_internal_links(self, subpage_tags: ResultSet[PageElement]) -> int:
        return len([link for link in subpage_tags if not self.is_external_link(link['href'])])

    def to_representation(self) -> dict:
        return {
            'url': self.url,
            'title': self.title,
            'internal links count': self._number_of_internal_links,
            'external links count': self._number_of_external_links,
            'reference count': self.reference_count
        }
