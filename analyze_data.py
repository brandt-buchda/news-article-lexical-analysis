import nltk
from parsearticlecontents import deserialize_article_data


def analyze_data(path):
    data = deserialize_article_data(path)
