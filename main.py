from scraper.api import ScraperAPI
from scraper.parser import ReviewsPageParser
from scraper.loader import ReviewsPageLoader
from flask import Flask, request, jsonify


loader = ReviewsPageLoader()
parser = ReviewsPageParser()
api = ScraperAPI(loader=loader, parser=parser)
server = Flask(__name__)


@server.route('/counts')
def get_review_counts():
    app_name = request.args.get('app', type=str)
    all_star_counts = api.get_review_counts(app_name=app_name)
    return jsonify(all_star_counts)


@server.route('/messages')
def get_review_data():
    app_name = request.args.get('app', type=str)
    page = request.args.get('page', default=1, type=int)
    reviews = api.get_reviews_on_page(app_name=app_name, page=page)
    return jsonify(reviews)


if __name__ == '__main__':
    server.run()
