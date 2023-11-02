from nltk.tokenize import wordpunct_tokenize
from lib.article import Article
from readability import Readability


def clean_data(article: Article):
    data = article.get_data()
    cleaned_data = []
    for cell in data:
        tokens = wordpunct_tokenize(cell)

        if len(tokens) > 5:
            cleaned_data.append(cell)

    article.set_data(cleaned_data)

def analyze_data(article):
    readability = Readability(article.get_metrics()[0]['raw_data'])

    article.metrics[0]["readability_score"] = readability.flesch()



