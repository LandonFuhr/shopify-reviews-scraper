import requests
from bs4 import BeautifulSoup


class ReviewsPageLoader:
    @staticmethod
    def _get_app_url(app_name: str, page: int) -> str:
        return f'https://apps.shopify.com/{app_name}/reviews?sort_by=recent&page={page}'

    @staticmethod
    def _get_page_content(url: str) -> bytes:
        return requests.get(url).content

    def fetch_page(self, app_name: str, page: int) -> BeautifulSoup:
        url = self._get_app_url(app_name=app_name, page=page)
        content = self._get_page_content(url=url)
        return BeautifulSoup(content, 'lxml')
