from urls.url import Url


class BaseUrl(Url):

    def __init__(self, base_url: str):
        self.url = base_url

    def to_string(self):
        return str(self.url)

    def __eq__(self, other):
        return self.url == other.url
