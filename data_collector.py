import requests
from bs4 import BeautifulSoup
from bs4.element import PageElement
from page_data import PageData


class DataCollector:

    def __init__(self):
        self.data = []
        self._urls = []

    @staticmethod
    def remove_forward_slash(url: str) -> str:
        if url and url[0] == '/':
            return url[1::]
        return url

    @staticmethod
    def remove_query_params(url: str):
        return url.split('?')[0]

    @staticmethod
    def contains_query_params(url: str):
        return '?' in url

    @staticmethod
    def remove_hash_sign(url: str):
        return url.split('#')[0]

    @staticmethod
    def contains_hash_sign(url: str):
        return '#' in url

    @staticmethod
    def is_relative_url(url: str):
        return url[:2] == '//'

    def print_sub_pages(self, subpage_name: str, num_of_subpages: int, depth: int, index: int, max_depth: int):
        if depth >= max_depth:
            print(f'\t \t {subpage_name}_{index} (0)')
        else:
            print(f'\t {subpage_name} ({num_of_subpages})')

        for num in range(num_of_subpages):
            self.print_sub_pages(f'subpage{index}', 0, depth+1, num+1, max_depth)

    def print_tree(self):
        for id, page in enumerate(self.data):
            num_of_subpages = page['internal links count']
            if id == 0:
                print(f"Main page ({num_of_subpages})")
            else:
                self.print_sub_pages(f'subpage{id}', num_of_subpages, 1, id, 2)

    def get_child_url(self, child: PageElement, base_url: str):
        child_url = child['href']
        if 'http' in child_url.split('/')[0]:
            print(f'HTTP -> {child_url}')
            child_url = ''
        else:
            if self.contains_query_params(child_url):
                child_url = self.remove_query_params(child_url)
            if self.contains_hash_sign(child_url):
                child_url = self.remove_hash_sign(child_url)
            if self.is_relative_url(child_url):
                child_url = 'https:' + child_url
            else:
                child_url = self.remove_forward_slash(child_url)
                child_url = base_url + child_url

        return child_url

    def _collect_data(self, base_url: str, parent_url: str, depth: int, max_depth: int):
        try:
            r = requests.get(parent_url, allow_redirects=False, timeout=5)
            soup = BeautifulSoup(r.content, 'html.parser')
        except Exception as e:
            print(e)
            return

        children = soup.find_all('a', href=True)

        try:
            title = soup.find('title').text
        except AttributeError:
            title = ''

        self._urls.append(parent_url)
        self.data.append({
            'url': parent_url,
            'title': title,
            'internal links count': len([link for link in children if not 'http' in link['href']]),
            'external links count': len([link for link in children if 'http' in link['href']]),
            'reference count': 0,
            'children': [self.get_child_url(child, base_url) for child in children]
        })

        depth += 1
        for child in children:
            child_url = self.get_child_url(child, base_url)
            if not child_url:
                continue
            if child_url in self._urls:
                print(f'EXISTING -> {child_url}')
            else:
                if depth >= max_depth:
                    continue
                print(f'NORMAL -> {child_url}')
                self._collect_data(base_url, child_url, depth, max_depth)

    def _update_data(self):
        for page in self.data:
            page['children'] = list(dict.fromkeys(page['children']))
            for child in page['children']:
                for p in self.data:
                    if p['url'] == child:
                        p['reference count'] += 1

        for page in self.data:
            page.pop('children')

    def get_page_data(self, base_url: str, max_depth: int = 2) -> PageData:
        
        self._collect_data(base_url, base_url, 0, max_depth)
        self._update_data()
