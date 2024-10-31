import sys
import os
import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            dbname='sap',
            user='meli',
            password='metralleta',
            host='db',
            port='5432'
        )
        return conn.cursor()
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def store_pass(username, email, password, url, app, cur):
    input = """
    INSERT INTO accounts (
        username, email, password, url, app, dob
    )
    VALUES (%s, %s, %s, %s, %s)
    """
    input_data = (
        username, email, password, url, app
    )
    cur.execute(input, input_data)

def del_pass(user, app, cur):
    input = """
    DELETE FROM accounts
        WHERE app = %s AND (username = %s OR email = %s)
    """
    input_data = (app, user, user)
    cur.execute(input, input_data)

conn.commit()
cur.close()
conn.close()
print("Password Manager Updated!", file=sys.stdout)
