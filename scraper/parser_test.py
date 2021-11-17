from bs4 import BeautifulSoup
from pathlib import Path
import pytest
from .parser import ReviewsPageParser
from .test_data.test_data import ExamplePage, EXAMPLE_PAGES


def get_relative_path(rel_path: str) -> str:
    return str(Path(Path(__file__).parent.resolve(), rel_path))


def get_test_soup(html_file_path: str) -> BeautifulSoup:
    real_path = get_relative_path(html_file_path)
    with open(real_path, 'r') as f:
        return BeautifulSoup(f, 'lxml')


@pytest.mark.parametrize('example_page', EXAMPLE_PAGES)
def test_review_star_counts(example_page: ExamplePage):
    soup = get_test_soup(example_page.file_path)
    parser = ReviewsPageParser()

    star_counts = parser.get_all_star_counts(soup)

    assert star_counts == example_page.stars_counts


@pytest.mark.parametrize('example_page', EXAMPLE_PAGES)
def test_all_reviews_single_page(example_page: ExamplePage):
    soup = get_test_soup(example_page.file_path)
    parser = ReviewsPageParser()

    reviews = parser.get_all_reviews_on_page(soup)

    assert reviews == example_page.reviews
