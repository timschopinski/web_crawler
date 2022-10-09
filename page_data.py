from typing import List

from bs4.element import PageElement, ResultSet


class PageData:

    def __init__(self):
        self.data = []

    @staticmethod
    def get_number_of_external_links(children: ResultSet[PageElement]):
        return len([link for link in children if 'http' in link['href']])

    @staticmethod
    def get_number_of_internal_links(children: ResultSet[PageElement]):
        return len([link for link in children if 'http' not in link['href']])

    def add_data(self, parent_url: str, title: str, children: ResultSet[PageElement], children_urls: List[str]):
        self.data.append({
            'url': parent_url,
            'title': title,
            'internal links count': self.get_number_of_internal_links(children),
            'external links count': self.get_number_of_external_links(children),
            'reference count': 0,
            'children': children_urls
        })