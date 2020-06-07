"""This module's docstring summary line.
pandas is used to import excel file.

global_env.read contains the name and path of tables.

global_env.basic_fun contains basic function of sqlite.
"""
import pandas as pd
from process_program.global_env.read import A
from process_program.global_env.basic_fun import drop_table


def init_basic_data(conn, table03):
    """Test for case study 1.
       Open the database connection and the Excel file
       Name of Excel xlsx file. SQLite database will have the same
       name and extension .db
    """
    drop_table(conn, table03)

    # create table03 and convert file SF_PSI_test_2019.xlsx into table03
    # wb_aniso=pd.read_excel('SF_PSI_test_2019.xlsx',sheet_name=None)
    wb_aniso = pd.read_excel(A.DB_FILE_PATH_1+'SF_PSI_test_2019.xlsx',
                             sheet_name=None)
    for sheet in wb_aniso:
        wb_aniso[sheet].to_sql(sheet, conn, index=False)
    conn.commit()
    print("initialization_basic_data is completed!")
