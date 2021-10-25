import sqlite3
from sqlite3 import Error
import pandas as pd
import random


def create_conn():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect('my_data.db')
    except Error as e:
        print(e)
    print("connection created.")
    return conn


def create_connection():
    connection = create_conn()
    # create_tables(connection)
    return connection


def select_article_by_mood(conn, mood_val):
    if mood_val == "\u0db1\u0dbb\u0d9a":
        mood = 'sad'
    elif mood_val == "\u0dc4\u0ddc\u0daf":
        mood = 'happy'
    else:
        mood = 'other'
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM article WHERE mood='{mood}'""")

    rows = cur.fetchall()

    result = []
    if len(rows) >= 5:
        for row in random.sample(rows, 5):
            result.append(row)
            print(row)
    return result


def select_all_therapists(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM therapist")

    rows = cur.fetchall()
    result = []
    for row in rows:
        print(row)
        result.append(row)
    return result


def create_tables(conn):
    cur1 = conn.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS article (title text, resource text, mood text)")

    cur2 = conn.cursor()
    cur2.execute(
        "CREATE TABLE IF NOT EXISTS therapist (name text, description text, title text, contactNo text, area text)")

    articles = pd.read_csv('/home/shehanaiqbal/Zone24x7/yana-chatbot/Yana/database/articles_data.csv')
    articles.to_sql('article', conn, if_exists='append', index=False)

    articles = pd.read_csv('/home/shehanaiqbal/Zone24x7/yana-chatbot/Yana/database/therapist_data.csv')
    articles.to_sql('therapist', conn, if_exists='append', index=False)


connection = create_connection()
create_tables(connection)


def create_connection():
    # create_tables(connection)
    return connection
