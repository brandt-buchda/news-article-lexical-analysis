from queryarticles import QueryDateRange


def main():
    #article_hrefs = QueryDateRange("1999-04-01", "1999-04-30")

    article_hrefs = {
        "",
        "",
        "",
        "",
        ""
    }

    for href in article_hrefs:
        ParseArticleContents(href)
    pass


if __name__ == '__main__':
    main()
