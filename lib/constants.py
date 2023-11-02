class Paths:
    ARTICLE_DIRECTORY = 'articles/'
    CSV_DIRECTORY = 'csv/'


class Newspapers:
    NEW_YORK_TIMES = {
        'project': 'NYT',
        'url': 'https://www.nytimes.com',
        'query-url': 'https://www.nytimes.com/search?',
        'query-terms': {
            'types': 'article',
            'sort': 'oldest',
            'sections': 'Opinion%7Cnyt%3A%2F%2Fsection%2Fd7a71185-aa60-5635-bce0-5fab76c7c297',
            'dropmab': 'false'},
        'query-results': 'query_results.csv'}


def get_project(newspaper):
    return newspaper['project']


def get_url(newspaper):
    return newspaper['url']


def get_query_url(newspaper):
    return newspaper['query-url']


def get_query_terms(newspaper):
    return newspaper['query-terms']


def get_query_results(newspaper):
    return newspaper['query-results']


def get_query_results_path(newspaper):
    return f'{Paths.CSV_DIRECTORY}{get_project(newspaper)}/{get_query_results(newspaper)}'

