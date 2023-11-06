import pandas
import readability.scorers
from nltk.tokenize import wordpunct_tokenize
from lib.article import Article
from readability import Readability
from pandas import DataFrame
import lib.utility

def clean_article_data(article: Article):
    data = article.get_data()
    cleaned_data = []
    for cell in data:
        tokens = wordpunct_tokenize(cell)

        if len(tokens) > 5:
            cleaned_data.append(cell)

    article.set_data(cleaned_data)


def compute_flesh_reading_score(articles):
    result = pandas.DataFrame(columns=['year', 'flesch_score'])  # Initialize an empty DataFrame with column names
    for article in articles:
            delimiter = " "

            try:
                raw_data = delimiter.join(article.get_data())
                r = Readability(raw_data)

                f = r.flesch()
            except:
                continue
            year = int(lib.utility.split_date(article.get_href())[0:4])  # Make sure to extract the correct year
            row = pandas.DataFrame([{'year': year, 'flesch_score': f.score}])
            result = pandas.concat([result, row], ignore_index=True)






    return result




