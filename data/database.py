import sqlite3

class UserLang():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def add_user_lang(self, user_id, lang):
        with self.connection:
            self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS 'users' (id INTEGER, lang TEXT, UNIQUE(id, lang) ON CONFLICT REPLACE)"""
            )

            self.cursor.execute(
                """INSERT INTO 'users' (id, lang) VALUES (?, ?) """, (user_id, lang,)
            )

    def get_lang(self, user_id):
        with self.connection:
            return self.cursor.execute(
                """SELECT lang FROM 'users' WHERE id =?""", (user_id,)
            ).fetchall()[0][0]


#test
# db = UserLang('data/user_languages.db')
# db.add_user_lang(user_id=121232, lang="en")
# db.add_user_lang(user_id=121237, lang="en")
