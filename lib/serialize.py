import csv
from lib.constants import get_query_results_path
from lib.article import Article
from lib.utility import *


class CsvSerialize:
    def __init__(self, newspaper, directory):
        self.extension = 'csv'
        self.newspaper = newspaper
        self.directory = directory

    def get_article_path(self, title):
        return f'{self.directory}{self.newspaper["project"]}/{title}.{self.extension}'

    def serialize_article_data(self, article: Article):
        with open(self.get_article_path(article.title), "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(["href", "title", "author", "paragraphs"])
            writer.writerow([article.get_href(), article.get_title(), article.get_author()] + article.get_data())

            if article.get_metrics() is not None:
                for row in article.get_metrics():
                    writer.writerow(row.keys())
                    writer.writerow(row.values())

    def deserialize_article_data(self, title: str) -> Article:
        with open(self.get_article_path(title), "r", newline='') as file:
            reader = csv.reader(file)

            for row in reader[1:]:
                href = row[0]
                title = row[1]
                author = row[2]
                paragraphs = []
                for paragraph in row[3:]:
                    paragraphs.append(paragraph)

                return Article(href, title, author, paragraphs)

    def serialize_query_results(self, hrefs):
        with open(get_query_results_path(self.newspaper), "w", newline='') as file:
            writer = csv.writer(file)

            keys = ["Title", "Date", "href"]
            writer.writerow(keys)

            for href in hrefs:
                values = []
                writer.writerow([split_title(href), split_date(href), href])

    def deserialize_query_results(self):
        with open(get_query_results_path(self.newspaper), "r", newline='') as file:
            reader = csv.DictReader(file)
            results = []

            for row in reader:
                results.append(row)

            return results

