import sqlite3
from pathlib import Path


def init():
    """
        Создание файла sqlite3
        """
    DB_NAME = 'db.sqlite3'
    DB_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()


def create_table():
    """
    Для создания таблиц
    """
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            info TEXT,
            link TEXT)
        """
    )
    db.commit()


def cars_done():
    cur.execute("""
    SELECT * FROM cars
    """)
    return cur.fetchall()


def get_cars(cars):
    """
        Заполнениние таблицы cars
    """
    cur.executemany("""INSERT INTO cars (
    name,
    price,
    info,
    link) VALUES (?, ?, ?, ?)""", cars)
    db.commit()