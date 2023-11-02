import sys
import time
from lib import constants
from lib.constants import *
from lib.parsehtlm import ParseHtml, parse_article_contents, query_date_range
from lib.serialize import CsvSerialize
from analyzedata import clean_data

parse_html = ParseHtml(Newspapers.NEW_YORK_TIMES, constants.Paths.ARTICLE_DIRECTORY)
csv_serialize = CsvSerialize(Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)


def query_nyt_article_database(start_year, end_year):
    hrefs = []
    for year in range(start_year, end_year):
        print("Searching: " + str(year))
        for month in range(1, 13):
            print("Month: " + str(month))
            hrefs.extend(query_date_range(
                f'{year}-{month:02d}-01',
                f'{year}-{month:02d}-28'))
            time.sleep(12)

    csv_serialize.serialize_query_results(hrefs)


def scrape_article_data():
    query_results = csv_serialize.deserialize_query_results()

    for result in query_results:
        article = parse_article_contents(result['href'])
        clean_data(article)
        csv_serialize.serialize_article_data(article)
        time.sleep(2)


def process_articles():
    articles = parse_html.parse_all_article_contents()

    for article in articles:
        clean_data(article)
        csv_serialize.serialize_article_data(article)


def main():
    query_nyt_article_database(int(sys.argv[1]), int(sys.argv[2]))

    scrape_article_data()


if __name__ == "__main__":
    main()
