from bs4 import BeautifulSoup


def ParseArticleContents(href, directory='articles/NYT/'):

    with open(directory + href) as article:
        page_contents = article.read()

        soup = BeautifulSoup(page_contents, 'html.parser')

        paragraphs = soup.find_all('p')

        for line in paragraphs:
            print(line.get_text())

