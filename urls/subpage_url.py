from bs4.element import PageElement
from urls.url import Url 


class SubpageUrl(Url):

    def __init__(self, base: Url, a_tag: PageElement):
        self.url = self.get_subpage_url(a_tag, base)

    @staticmethod
    def _is_external_link(link) -> bool:
        return 'http' in link

    @staticmethod
    def _remove_forward_slash(url: str) -> str:
        if url and url[0] == '/':
            return url[1::]
        return url

    @staticmethod
    def _remove_query_params(url: str):
        return url.split('?')[0]

    @staticmethod
    def _contains_query_params(url: str):
        return '?' in url

    @staticmethod
    def _remove_hash_sign(url: str):
        return url.split('#')[0]

    @staticmethod
    def _contains_hash_sign(url: str):
        return '#' in url

    @staticmethod
    def _is_relative_path(path: str):
        return path[:2] == '//'

    def to_string(self):
        return str(self.url)

    def _get_validated_subpage_path(self, subpage_path: str) -> str:
        if self._contains_query_params(subpage_path):
            subpage_path = self._remove_query_params(subpage_path)
        if self._contains_hash_sign(subpage_path):
            subpage_path = self._remove_hash_sign(subpage_path)
        return subpage_path

    def _get_url_from_path(self, base: Url, path: str) -> str:
        if self._is_relative_path(path):
            url = 'https:' + path
        else:
            subpage_path = self._remove_forward_slash(path)
            url = base.to_string() + subpage_path

        return url

    def get_subpage_url(self, subpage_tag: PageElement, base: Url) -> str:
        subpage_path = subpage_tag['href']

        if self._is_external_link(subpage_path.split('/')[0]):
            subpage_url = ''
        else:
            validated_path = self._get_validated_subpage_path(subpage_path)
            subpage_url = self._get_url_from_path(base, validated_path)
        return subpage_url

