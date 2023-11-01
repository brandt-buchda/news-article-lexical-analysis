import constants
from parsehtlm import ParseHtml
from serialize import CsvSerialize
import analyzedata

def main():

    parse_html = ParseHtml(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.ARTICLE_DIRECTORY)
    csv_serialize = CsvSerialize(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)

    hrefs = []
    for year in range(1990, 2023):
        for month in range(1, 12):
            hrefs.extend(parse_html.query_date_range(
                f'{year}-{month:02d}-01',
                f'{year}-{month:02d}-28'))

    with open("csv/NYT/search.csv", "w") as results:
        for href in hrefs:
            results.write(href + ", ")

    article_hrefs = parse_html.parse_search_contents()

    pass

    articles = []
    for href in article_hrefs:
        article = parse_html.parse_article_contents(href)
        analyzedata.clean_data(article)
        analyzedata.analyze_data(article)
        articles.append(article)

    for article in articles:
        csv_serialize.serialize_article_data(article)


if __name__ == '__main__':
    main()
