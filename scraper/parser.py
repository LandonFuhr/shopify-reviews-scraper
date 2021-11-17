from __future__ import annotations
from typing import List
from dataclasses import dataclass
from bs4 import BeautifulSoup, element


@dataclass
class Review:
    store: str
    stars: int
    content: str
    date_str: str

    @classmethod
    def from_listing(cls, listing: element.Tag):
        return cls(
            store=listing.select('.review-listing-header')[0].text.strip(),
            stars=int(listing.select('.ui-star-rating')
                      [0].attrs['data-rating']),
            content=listing.select(
                '.review-content .truncate-content-copy')[0].text.strip(),
            date_str=listing.select(
                '.review-metadata__item .review-metadata__item-value')[1].text.strip()
        )


@dataclass
class StarCounts:
    total: int
    one_stars: int
    two_stars: int
    three_stars: int
    four_stars: int
    five_stars: int
    stars_count_list: List[int]
    average_rating: float

    @staticmethod
    def from_list(rating_counts: List[int], average_rating: float) -> StarCounts:
        return StarCounts(
            total=sum(rating_counts),
            one_stars=rating_counts[0],
            two_stars=rating_counts[1],
            three_stars=rating_counts[2],
            four_stars=rating_counts[3],
            five_stars=rating_counts[4],
            stars_count_list=rating_counts.copy(),
            average_rating=average_rating
        )


class ReviewsPageParser:
    def _get_stars_with_rating(self, rating: int, soup: BeautifulSoup) -> int:
        reviews_els = soup.select(f'a[href*="rating={rating}"]')
        reviews_count = 0
        if len(reviews_els) == 1:
            reviews_string = reviews_els[0].text
            reviews_count = int(reviews_string.strip('()'))
        return reviews_count

    def _get_average_rating(self, soup: BeautifulSoup) -> float:
        average_rating_els = soup.select('.ui-star-rating__rating')
        # e.g. "4.9 of 5 stars"
        rating_with_denominator = average_rating_els[0].text
        rating_text = rating_with_denominator.split()[0]
        return float(rating_text)

    def get_all_star_counts(self, soup: BeautifulSoup) -> StarCounts:
        star_counts_list = [self._get_stars_with_rating(
            rating=rating, soup=soup) for rating in [1, 2, 3, 4, 5]]
        average_rating = self._get_average_rating(soup=soup)
        return StarCounts.from_list(rating_counts=star_counts_list, average_rating=average_rating)

    def get_all_reviews_on_page(self, soup: BeautifulSoup) -> List[Review]:
        listings = soup.select('.review-listing')
        return [Review.from_listing(listing) for listing in listings]
