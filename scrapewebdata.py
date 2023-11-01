import constants
from constants import *
from parsehtlm import ParseHtml


def main():
    parse_html = ParseHtml(Newspapers.NEW_YORK_TIMES, constants.Paths.ARTICLE_DIRECTORY)

    # Query NYT article database from 1985 to present. Select 10 articles per month.
    hrefs = []
    for year in range(2022, 2023):
        for month in range(1, 12):
            hrefs.extend(parse_html.query_date_range(
                f'{year}-{month:02d}-01',
                f'{year}-{month:02d}-28'))



if __name__ == "__main__":
    main()
