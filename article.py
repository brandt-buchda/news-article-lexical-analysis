class Article:
    def __init__(self, href, title, author, data):
        self.href = href
        self.title = title
        self.author = author
        self.data: list[str] = data

    def get_href(self):
        return self.href

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_data(self):
        return self.data

