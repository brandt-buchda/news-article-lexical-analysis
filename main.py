from parsearticlecontents import parse_article_contents
from queryarticles import QueryDateRange


def main():
    #article_hrefs = QueryDateRange("1999-04-01", "1999-04-30")

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

    for href in article_hrefs:
        parse_article_contents(href)
    pass


if __name__ == '__main__':
    main()
