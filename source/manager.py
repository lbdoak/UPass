import sys
import psycopg2
from datetime import datetime
import os

def connect():
    try:
        conn = psycopg2.connect(
            dbname='sap',
            user='meli',
            password='metralleta',
            host='0.0.0.0',
            port='5432'
        )
        return conn
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def store_pass(username, email, password, url, app, conn):
    cur = conn.cursor()

    try:
        input = """
        INSERT INTO accounts (
            username, email, password, url, app, dob
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        input_data = (
            username, email, password, url, app, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        cur.execute(input, input_data)
        conn.commit()
        cur.close()
        conn.close()
        print(('-'*12) + 'CREATE' + ('-' *12), file=sys.stdout)
        print("\nEntries inserted for", app, "<----\n", file=sys.stdout)
        print('-'*30, file=sys.stdout)
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def del_pass(user, app, conn):
    cur = conn.cursor()
    try:
        input = """
        DELETE FROM accounts
            WHERE app = %s AND (username = %s OR email = %s)
        """
        input_data = (app, user, user)
        cur.execute(input, input_data)
        conn.commit()
        cur.close()
        conn.close()
        
        print(('-'*12) + 'DELETE' + ('-' *12), file=sys.stdout)
        print("\nEntries deleted for", app, "<----\n", file=sys.stdout)
        print('-'*30, file=sys.stdout)
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def find_user(user, conn):
    cur = conn.cursor()
    try:
        input = "SELECT * FROM accounts WHERE username = %s"
        cur.execute(input, (user,))
        conn.commit()
        res = cur.fetchall()
        input = "SELECT * FROM accounts WHERE email = %s"
        cur.execute(input, (user,))
        conn.commit()
        res += cur.fetchall()
        format_data(res)
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def find_pass(password, conn):
    cur = conn.cursor()
    try:
        input = """ SELECT * FROM accounts WHERE password = '""" + password + "'"
        cur.execute(input, password)
        conn.commit()
        res = cur.fetchall()
        format_data(res)
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def find_all(conn):
    cur = conn.cursor()
    try:
        input = """ SELECT * FROM accounts"""
        cur.execute(input)
        conn.commit()
        res = cur.fetchall()
        format_data(res)
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def empty(conn, fp='../source/usr/!'):
    cur = conn.cursor()
    try:
        input = """
        TRUNCATE TABLE accounts
        """
        cur.execute(input)
        conn.commit()
        cur.close()
        conn.close()
        if os.path.exists(fp):
            os.remove(fp)
    except (Exception, psycopg2.Error) as e:
        print(e, file=sys.stdout)

def format_data(res):
    form = ('User: ', 'Email: ', 'Password: ', 'Url: ', 'App: ', 'Date Added: ')
    
    for row in res:
        for i in range(0, len(row)):
            print(form[i] + str(row[i]))
        print('-'*30)
    print('')