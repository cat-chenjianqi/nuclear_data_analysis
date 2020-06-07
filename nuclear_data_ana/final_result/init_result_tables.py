import sqlite3
from process_program.global_env.read import A
from process_program.global_env.all_tables import *
from process_program.global_env.basic_fun import *
from itertools import islice
import pandas as pd 
import re


def init_result_tables(conn,table21,table22,table23):

    c=get_cursor(conn)	
    drop_table(conn, table21)
    drop_table(conn, table22)
    drop_table(conn, table23)
    # create table8	
    create_table(conn, create_table21_sql)
    create_table(conn, create_table22_sql)
    create_table(conn, create_table23_sql)
    conn.commit()
    conn.close()
    print("initialization_final_data is success!")
