import os
import sqlite3
from utils import code_generator


class SQL_LITE:
    def __init__(self, db_path=os.path.join(os.curdir, 'record.db')):
        self.connection = None
        # db_path_default = os.path.join(os.curdir, 'record.db')

        self._connect(db_path)
        self._ensure_db_scheme()

    def _connect(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self._ensure_db_scheme()

    def _ensure_db_scheme(self):
        sql = """CREATE TABLE IF NOT EXISTS redirect
            (code text, link text)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)

    def save_url(self, url):
        code = code_generator(6)
        cursor = self.connection.cursor()
        cursor.execute(
            """INSERT INTO redirect VALUES ('{}', '{}')""".format(code, url)
        )

        self.connection.commit()
        return True, code

    def get_url(self, code):
        cursor = self.connection.cursor()
        sql = "SELECT link FROM redirect WHERE code=?"
        cursor.execute(sql, [(code)])
        res = cursor.fetchone()
        if res is not None:
            return res[0]
        return res


class IN_MEMORY:
    def __init__(self):
        self._connect()

    def _connect(self):
        self.url_map = {}

    def save_url(self, url):
        code = code_generator(6)
        self.url_map[code] = url
        return True, code

    def get_url(self, code):
        return self.url_map[code]


class Database(SQL_LITE, IN_MEMORY):
    def __init__(self, use_external_db=False, db_path=os.path.join(os.curdir, 'record.db')):
        if use_external_db:
            SQL_LITE.__init__(self, db_path)
        else:
            IN_MEMORY.__init__(self)

    def save_url(self, url):
        return super().save_url(url)

    def get_url(self, code):
        return super().get_url(code)
