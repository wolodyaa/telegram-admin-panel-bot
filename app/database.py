import sqlite3
from assets.config import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_id integer PRIMARY KEY,
        username str,
        name str,
        surname str
        )""")


def register(user_id: int, username, name: str, surname: str):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("INSERT OR REPLACE INTO users(user_id, username, name, surname) VALUES(?, ?, ?, ?)", (user_id, username, name, surname))


def get_reg_data(user_id: int):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("SELECT name FROM users WHERE user_id = ? ORDER BY rowid DESC LIMIT 1", (user_id,))

        result = c.fetchone()

        if result:
            return result[0]
        else:
            return None


def get_data(username: str):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("SELECT user_id, name, surname FROM users WHERE username = ? ORDER BY rowid DESC LIMIT 1", (username,))

        result = c.fetchone()

        return result



def get_usernames():

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("SELECT username FROM users ORDER BY rowid DESC")

        result = c.fetchall()

        return result