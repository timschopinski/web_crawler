from typing import List


class Page:

    def __init__(self, url: str, title: str, subpages_urls: List[str]):
        self.url = url
        self.title = title
        self.subpages_urls = subpages_urls
        self._number_of_internal_links = self._count_internal_links()
        self._number_of_external_links = self._count_external_links()
        self.reference_count = 0

    @staticmethod
    def is_external_link(link) -> bool:
        return 'http' in link

    def get_unique_subpages_urls(self) -> List[str]:
        return list(dict.fromkeys(self.subpages_urls))

    def _count_external_links(self) -> int:
        return len([link for link in self.subpages_urls if self.is_external_link(link)])

    def _count_internal_links(self) -> int:
        return len([link for link in self.subpages_urls if not self.is_external_link(link)])

    def to_representation(self) -> dict:
        return {
            'url': self.url,
            'title': self.title,
            'internal links count': self._number_of_internal_links,
            'external links count': self._number_of_external_links,
            'reference count': self.reference_count
            }
