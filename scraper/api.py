from typing import List
from scraper.parser import ReviewsPageParser
from .loader import ReviewsPageLoader
from .parser import Review, ReviewsPageParser, StarCounts


class ScraperAPI:
    def __init__(self, loader: ReviewsPageLoader, parser: ReviewsPageParser) -> None:
        self._loader = loader
        self._parser = parser

    def get_review_counts(self, app_name: str) -> StarCounts:
        soup = self._loader.fetch_page(app_name=app_name, page=1)
        return self._parser.get_all_star_counts(soup=soup)

    def get_reviews_on_page(self, app_name: str, page: int) -> List[Review]:
        soup = self._loader.fetch_page(app_name=app_name, page=page)
        return self._parser.get_all_reviews_on_page(soup=soup)
