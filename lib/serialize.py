import csv
import os
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
        with open(self.get_article_path(title), "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                href = row['href']
                title = row['title']
                author = row['author']
                paragraphs = [row['paragraphs']]
                if None in row:
                    for paragraph in row[None]:
                        paragraphs.append(paragraph)

                return Article(href, title, author, paragraphs)

    def load_all_article_data(self):
        csv_path = f'{self.directory}{self.newspaper["project"]}/'

        articles = []

        for file in os.listdir(csv_path):
            articles.append(self.deserialize_article_data(file.split('.')[0]))

        return articles



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

