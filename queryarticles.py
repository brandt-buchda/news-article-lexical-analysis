from copywebarticle import  CopyWebArticle

queryTerms = {
    'types': 'article',
    'sort': 'oldest',
    'sections': 'Opinion%7Cnyt%3A%2F%2Fsection%2Fd7a71185-aa60-5635-bce0-5fab76c7c297'}

nyt_article_search_url = 'https://www.nytimes.com/search?'


def QueryDateRange(start_date, end_date, n=10):
    """Queries the NYT database for articles in the date range and returns the first n hrefs
    Parameters
    ----------
    start_date
        The beginning date of the date range query

    end_date
        The ending date of the date range query

    n
        The maximum number of articles to return

    Returns
    -------
    list
        A list of strings representing article hrefs

    """

    # TODO Query NYT article search base
    query_url = nyt_article_search_url

    for key, value in queryTerms.items():
        query_url += "&" + key + "=" + value

    query_url += "&startDate" + start_date
    query_url += "&endDate" + end_date

    CopyWebArticle(query_url)

    for i in range(0, n):
        pass

    pass
