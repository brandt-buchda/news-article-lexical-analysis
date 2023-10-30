from pywebcopy import save_webpage
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
        kwargs = {'bypass_robots': True, "project_name": self.newspaper}
        save_webpage(href, self.directory, **kwargs, open_in_browser=False)

    def parse_article_contents(self, href):
        self.copy_web_article(href)

        article_path = f'{self.directory}{self.newspaper}/{strip_http(href)}'

        with open(article_path) as article:
            page_contents = article.read()

            text = BeautifulSoup(page_contents, 'html.parser').find_all('p')
            paragraphs = []

            for paragraph in text:
                paragraphs.append(paragraph.get_text())

            return Article(href, strip_article_name(href), "Unknown", paragraphs)
