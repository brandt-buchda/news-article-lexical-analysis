import constants
import serialize
from parsehtlm import ParseHtml
from serialize import CsvSerialize

def main():
    #article_hrefs = QueryDateRange("1999-04-01", "1999-04-30")

    parse_html = ParseHtml(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.ARTICLE_DIRECTORY)
    csv_serialize = CsvSerialize(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)

    article_hrefs = {
        "https://www.nytimes.com/1999/04/29/opinion/IHT-the-colorado-shooting-letters-to-the-editor.html",
        "https://www.nytimes.com/1999/04/29/opinion/a-german-italian-merger.html",
        "https://www.nytimes.com/1999/04/29/opinion/essay-the-deadliest-download.html",
        "https://www.nytimes.com/1999/04/29/opinion/IHT-yes-to-kosovo-no-to-east-timor.html",
        "https://www.nytimes.com/1999/04/29/opinion/yes-im-in-a-clique.html",
        "https://www.nytimes.com/2023/10/22/opinion/haiti-dominican-racism-immigration.html",
        "https://www.nytimes.com/2023/10/21/opinion/pedestrians-cars-trucks-suvs-death.html",
        "https://www.nytimes.com/2023/10/21/opinion/aging-prison.html",
        "https://www.nytimes.com/2023/10/21/opinion/silence-social-media-conflict.html",
        "https://www.nytimes.com/2023/10/20/opinion/harvard-penn-donors.html"
    }

    articles = []

    for href in article_hrefs:
        articles.append(parse_html.parse_article_contents(href))
    pass

    for article in articles:
        csv_serialize.serialize(article)


if __name__ == '__main__':
    main()
