import time
import os
import requests
from pywebcopy import save_webpage
from pywebcopy.parsers import MultiParser
from bs4 import BeautifulSoup
from article import Article


def strip_http(href):
    return href.split("https://")[1]


def strip_article_name(href):
    split = href.split("/")

    return f'{split[len(split) - 1].split(".")[0]}'


class ParseHtml:
    def __init__(self, newspaper, directory):
        self.newspaper = newspaper
        self.directory = directory

    def copy_web_article(self, href):
        kwargs = {'bypass_robots': True, "project_name": self.newspaper["project"]}
        save_webpage(href, self.directory, **kwargs, open_in_browser=False)

    def parse_search_contents(self):

        article_path = f'{self.directory}{self.newspaper["project"]}/{strip_http(self.newspaper["url"])}/'

        search_results = []

        for file in os.listdir(article_path):
            if file.endswith("html") and "search" in file:
                with open(article_path + file) as article:
                    page_contents = article.read()

                    text = BeautifulSoup(page_contents, 'html.parser').find_all('a', href=True)
                    hrefs = []

                    for href in text:
                        if "searchResultPosition" in href['href']:
                            hrefs.append(self.newspaper['url'] + href['href'].split("?")[0])

                    search_results.extend(hrefs)

        return search_results

    def query_date_range(self, start_date, end_date, n=10):
        # TODO Query NYT article search base
        query_url = self.newspaper["query-url"]

        for key, value in self.newspaper["query-terms"].items():
            query_url += "&" + key + "=" + value

        query_url += "&startDate" + start_date
        query_url += "&endDate" + end_date

        time.sleep(0.5)
        request = requests.get(query_url)

        html = request.content

        text = BeautifulSoup(html, 'html.parser').find_all('a', href=True)
        hrefs = []

        for href in text:
            if "searchResultPosition" in href['href']:
                hrefs.append(self.newspaper['url'] + href['href'].split("?")[0])

        return hrefs

    def parse_article_contents(self, href):
        self.copy_web_article(href)

        article_path = f'{self.directory}{self.newspaper["project"]}/{strip_http(href)}'

        with open(article_path) as article:
            page_contents = article.read()

            text = BeautifulSoup(page_contents, 'html.parser').find_all('p')
            paragraphs = []

            for paragraph in text:
                paragraphs.append(paragraph.get_text())

            return Article(href, strip_article_name(href), "Unknown", paragraphs)
