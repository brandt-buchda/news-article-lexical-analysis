from pywebcopy import save_webpage


def copy_web_article(url, directory, project):

    kwargs = {'bypass_robots': True, "project_name": project}
    save_webpage(url, directory, **kwargs, open_in_browser=False)
