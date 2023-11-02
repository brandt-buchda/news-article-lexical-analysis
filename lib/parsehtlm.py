import time
import os
import requests
from lib.utility import *
from pywebcopy import save_webpage
from bs4 import BeautifulSoup
from lib.article import Article


def query_date_range(start_date, end_date, n=10):
    search_params = {
        'api-key': "FILL WITH API KEY",
        'begin_date': start_date,
        'end_date': end_date,
        'sort': 'oldest',
        'fl': 'web_url',
        'fq': 'section_name:("Opinion")',
        'page': 0
    }

    response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json", params=search_params)

    data = response.json()
    hrefs = [doc['web_url'] for doc in data['response']['docs']]

    return hrefs


def parse_article_contents(href):

    request = requests.get(href)
    time.sleep(1)

    soup = BeautifulSoup(request.content, 'html.parser')
    text = soup.find_all('p')
    paragraphs = []

    for paragraph in text:
        paragraphs.append(paragraph.get_text())

    return Article(href, split_title(href), "Unknown", paragraphs)


class ParseHtml:
    def __init__(self, newspaper, directory):
        self.newspaper = newspaper
        self.directory = directory

    def copy_web_article(self, href):
        kwargs = {'bypass_robots': True, "project_name": self.newspaper["project"]}
        save_webpage(href, self.directory, **kwargs, open_in_browser=False)

    def parse_all_article_contents(self):
        article_path = f'{self.directory}{self.newspaper["project"]}/{strip_http(self.newspaper["url"])}/'

        articles = []
        for file in os.listdir(article_path):
            if file.endswith("html"):
                with open(article_path + file, encoding='utf-8', errors='ignore') as article:

                    soup = BeautifulSoup(article.read(), 'html.parser')

                    href = soup.find('meta', {'property': 'og:url'}).get('content')

                    text = soup.find_all('p')
                    paragraphs = []

                    for paragraph in text:
                        paragraphs.append(paragraph.get_text())

                    articles.append(Article(href, split_title(href), "Unknown", paragraphs))

        return articles
