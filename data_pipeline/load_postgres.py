import psycopg2
import json
import os
from dotenv import load_dotenv

load_dotenv()

def load_data_to_postgres():
    with open('posts.json') as f:
        posts = json.load(f)
    with open('users.json') as f:
        users = json.load(f)

    conn = psycopg2.connect(
        host=os.getenv("PG_HOST"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD")
    )
    cur = conn.cursor()

    # Drop and recreate tables (optional but safe for dev)
    cur.execute("DROP TABLE IF EXISTS raw_users")
    cur.execute("DROP TABLE IF EXISTS raw_posts")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_users (
            id INT PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            phone TEXT,
            website TEXT,
            address TEXT,
            company TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_posts (
            id INT PRIMARY KEY,
            userid INT,
            title TEXT,
            body TEXT
        )
    """)

    for user in users:
        cur.execute("""
            INSERT INTO raw_users (id, name, username, email, phone, website, address, company)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            user['id'],
            user['name'],
            user['username'],
            user['email'],
            user['phone'],
            user['website'],
            json.dumps(user['address']),   # convert dict to string
            json.dumps(user['company'])    # convert dict to string
        ))

    for post in posts:
        cur.execute("""
            INSERT INTO raw_posts (id, userid, title, body)
            VALUES (%s, %s, %s, %s)
        """, (
            post['id'],
            post['userId'],  # keep lowercase `userid` to match table schema
            post['title'],
            post['body']
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded into PostgreSQL")

if __name__ == "__main__":
    load_data_to_postgres()
