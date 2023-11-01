import csv
from constants import get_query_results_path
from article import Article


class CsvSerialize:
    def __init__(self, newspaper, directory):
        self.extension = 'csv'
        self.newspaper = newspaper
        self.directory = directory

    def get_article_path(self, title):
        return f'{self.directory}{self.newspaper["project"]}/{title}.{self.extension}'

    def serialize_article_data(self, article: Article):
        with open(self.get_article_path(article.title), "w", newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["href", "title", "author", "paragraphs"])
            writer.writerow([article.get_href(), article.get_title(), article.get_author()] + article.get_data())

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
        with open(get_query_results_path(Newspapers.NEW_YORK_TIMES), "w") as results:
            for href in hrefs:
                results.write(href + ", ")

    def deserialize_query_results(self):
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


