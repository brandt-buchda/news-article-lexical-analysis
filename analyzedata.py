import readability.scorers
from nltk.tokenize import wordpunct_tokenize
from article import Article
from readability import Readability

def clean_data(article: Article):
    # Prune cell data
    metrics = [{'raw_data': ""}]

    for cell in article.get_data():
        metrics[0]['raw_data'] += cell
        tokens = wordpunct_tokenize(cell)

        if len(tokens) > 5:
            metrics.append({'word_count': len(tokens), 'tokens': tokens})

    article.set_metrics(metrics)


def analyze_data(article):
    readability = Readability(article.get_metrics()[0]['raw_data'])

    article.metrics[0]["readability_score"] = readability.flesch()



