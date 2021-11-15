from dataclasses import dataclass
from typing import List
from ..parser import StarCounts, Review


@dataclass
class ExamplePage:
    name: str
    file_path: str
    stars_counts: StarCounts
    reviews: List[Review]


EXAMPLE_PAGES = [
    ExamplePage(
        name='yotpo',
        file_path='./test_data/yotpo.html',
        stars_counts=StarCounts(
            total=3999,
            one_stars=150,
            two_stars=49,
            three_stars=37,
            four_stars=173,
            five_stars=3590,
            stars_count_list=[150, 49, 37, 173, 3590],
            average_rating=4.9
        ),
        reviews=[
            Review(
                store='Test Store 1',
                stars=5,
                content='Test content 1',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 2',
                stars=5,
                content='Test content 2',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 3',
                stars=5,
                content='Test content 3',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 4',
                stars=5,
                content='Test content 4',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 5',
                stars=5,
                content='Test content 5',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 6',
                stars=5,
                content='Test content 6',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 7',
                stars=5,
                content='Test content 7',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 8',
                stars=5,
                content='Test content 8',
                date_str='November 11, 2021'
            ),
            Review(
                store='Test Store 9',
                stars=5,
                content='Test content 9',
                date_str='November 10, 2021'
            ),
            Review(
                store='Test Store 10',
                stars=5,
                content='Test content 10',
                date_str='November 10, 2021'
            )
        ]
    ),  # YOTPO
    ExamplePage(
        name='govalo',
        file_path='./test_data/govalo.html',
        stars_counts=StarCounts(
            total=2,
            one_stars=0,
            two_stars=0,
            three_stars=0,
            four_stars=0,
            five_stars=2,
            stars_count_list=[0, 0, 0, 0, 2],
            average_rating=5.0
        ),
        reviews=[
            Review(
                store='Fake Store 1',
                stars=5,
                content='Fake content 1',
                date_str='October 21, 2021'
            ),
            Review(
                store='Fake Store 2',
                stars=5,
                content='Fake content 2',
                date_str='October 7, 2021'
            )
        ]
    )  # GOVALO
]
