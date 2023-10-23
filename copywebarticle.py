from pywebcopy import save_webpage
from directoryconstants import *


def CopyWebArticle(url):

    kwargs = {'bypass_robots': True, "project_name": "NYT"}
    save_webpage(url, ARTICLE_DIRECTORY, **kwargs)
