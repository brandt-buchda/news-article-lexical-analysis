
def strip_http(href):
    return href.split("https://")[1]


def split_title(href):
    split = href.split("/")

    return f'{split[len(split) - 1].split(".")[0]}'


def split_date(href):
    split = strip_http(href).split("/")
    return f'{split[1]}-{split[2]}-{split[3]}'
