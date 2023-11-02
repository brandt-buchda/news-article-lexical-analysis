from lib import constants
from lib.parsehtlm import ParseHtml
from lib.serialize import CsvSerialize
import analyzedata

def main():

    parse_html = ParseHtml(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.ARTICLE_DIRECTORY)
    csv_serialize = CsvSerialize(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)

    query_results = csv_serialize.deserialize_query_results()

    articles = []
    for result in query_results:
        article = parse_article_contents(result['href'])
        analyzedata.clean_data(article)
        analyzedata.analyze_data(article)
        articles.append(article)

    for article in articles:
        csv_serialize.serialize_article_data(article)


if __name__ == '__main__':
    main()
