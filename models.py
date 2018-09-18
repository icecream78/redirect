from utils import code_generator


class Database:
    def __init__(self):
        self.url_map = {}

    def save_url(self, url):
        code = code_generator(6)
        self.url_map[code] = url
        return True, code

    def get_url(self, code):
        return self.url_map[code]
