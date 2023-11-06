import pandas
from nltk.tokenize import wordpunct_tokenize
from readability import Readability
from lib.article import Article
import lib.utility

def compute_flesh_reading_score(articles):
    result = pandas.DataFrame(columns=['year', 'flesch_score'])
    for article in articles:
        delimiter = " "
        try:
            raw_data = delimiter.join(article.get_data())
            flesch = Readability(raw_data).flesch()
        except:  # Readability may throw an exception if the data is too short
            continue
        year = int(lib.utility.split_date(article.get_href())[0:4])
        row = pandas.DataFrame([{'year': year, 'flesch_score': flesch.score}])
        result = pandas.concat([result, row], ignore_index=True)

    return result


def clean_article_data(article: Article):
    data = article.get_data()
    cleaned_data = []
    for cell in data:
        tokens = wordpunct_tokenize(cell)

        if len(tokens) > 5:
            cleaned_data.append(cell)

    article.set_data(cleaned_data)

