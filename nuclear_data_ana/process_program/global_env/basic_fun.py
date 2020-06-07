"""This module's docstring summary line.
datatime is included to extract the time difference between
start time and end time.
"""
import sqlite3
import os

import re


# determine statement of printing sql
SHOW_SQL = False


def get_conn(path):
    """connect with the database
    """
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        return conn
    else:
        conn = None
        print('In memory:[:memory:]')
        return sqlite3.connect(':memory:')


def get_cursor(conn):
    """get the cursor of database.
    """
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


def close_all(conn, c):
    """close all connection with database.
    """
    try:
        if c is not None:
            conn.commit()
            c.close()
    finally:
        if c is not None:
            conn.commit()
            c.close()


def create_table(conn, sql):
    """create table in database.
    """
    table_string_1 = re.split('id', sql)
    table_string_2 = re.split('TABLE', table_string_1[0])
    table_string_3 = re.sub(r'\W', "", table_string_2[1])
    if sql is not None:
        if SHOW_SQL:
            print('execute sql:[{}]'.format(table_string_3))
        c = get_cursor(conn)
        c.execute(sql)
        conn.commit()
        print('create table [{}] successfully!'.format(table_string_3))
        close_all(conn, c)
    else:
        print('the [{}] is not empty and equal None!'.format(sql))


def drop_table(conn, table):
    """drop table in database.
    """
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('execute sql:[{}]'.format(sql))
        c = get_cursor(conn)
        c.execute(sql)
        conn.commit()
        print('delete table [{}] successfully!'.format(table))
        close_all(conn, c)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
