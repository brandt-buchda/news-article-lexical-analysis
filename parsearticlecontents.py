from bs4 import BeautifulSoup
from constants import *
from copywebarticle import copy_web_article
import csv


def strip_http(href):
    return href.split("https://")[1]


def strip_article_name(href):
    split = href.split("/")

    return f'{split[len(split) - 1].split(".")[0]}.csv'


def parse_article_contents(href, project=Newspapers.NEW_YORK_TIMES):
    copy_web_article(href, Paths.ARTICLE_DIRECTORY, project)

    article_path = f'{Paths.ARTICLE_DIRECTORY}{project}/{strip_http(href)}'
    csv_path = f'{Paths.CSV_DIRECTORY}{project}/{strip_article_name(href)}'

    print(csv_path)

    with open(article_path) as article:
        page_contents = article.read()

        paragraphs = BeautifulSoup(page_contents, 'html.parser').find_all('p')

        data = Csv()
        for line in paragraphs:
            data.data['paragraphs'].append(line.get_text())

    serialize_article_data(data, csv_path)


def serialize_article_data(data: Csv, path):
    csv_file = open(path, "w", newline='')
    csv_writer = csv.writer(csv_file)

    values: list[str] = [data.data['title'], data.data['author']]
    values[len(values):] = data.data['paragraphs']

    csv_writer.writerow(data.data)
    csv_writer.writerow(values)

def deserialize_article_data(path):
    csv_file = open(path, "w", newline='')

    pass