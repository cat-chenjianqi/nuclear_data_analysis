"""This module's docstring summary line.
datatime is included to extract the time difference between
start time and end time.
"""
import os

from itertools import islice
from datetime import datetime
import numpy as np

from process_program.global_env.read import A
from process_program.global_env.all_tables import create_table01_sql
from process_program.global_env.basic_fun import get_cursor, drop_table, create_table

class GlobalTest:
    """class GlobalTest is used to set global parameter here.
       it is used to obtain variable of n_files.
    """
    # Encapsulate the global variables into objects
    def __init__(self, x):
        self.n_files = x


def each_file(filepath, list_total, args):
    """each_file is used to traverse the .setup files in specify directory.
    """
    n_files = 0
    # obtain the file name under current directory and return list
    path_dir = os.listdir(filepath)
    for file_name in path_dir:
        # write the file name behind the current directory
        new_dir = os.path.join(filepath, file_name)
        # determine if it is setup file
        if os.path.splitext(new_dir)[1] == ".setup":
            list_total.append(file_name.split('.')[0])   # list0
            read_file(new_dir, list_total)
            n_files = n_files+1
    args.n_files = n_files
        # return n_files


def read_file(filepath, list_total):
    """read_file is used to extract the corresponding time info of every file.
    """
    with open(filepath, "r") as file_bin:
        line_temp = file_bin.readline()
        line = file_bin.readline()  # The first line is blank, so I need to read twice
        while line:
            # extract data according to keywords.
            if line[:18] == '- Event count  : 0':
                data1, time1 = file_bin.readline().split()[-2:]
                start = data1+' '+time1
                start = datetime.strptime(start, '%d-%m-%Y %H:%M:%S')
                list_total.append(str(start))   # start time
                data2, time2 = file_bin.readline().split()[-2:]
                stop = data2 + ' ' + time2
                stop = datetime.strptime(stop, '%d-%m-%Y %H:%M:%S')
                list_total.append(str(stop))   # stop time
                time_dif = (stop-start).total_seconds()  # time unit second
                # write() argument must be str, not datetime.datetime
                list_total.append(str(time_dif))
            line = file_bin.readline()
        # return list_total


def convert_time_info_into_file():
    """convert_time_info_into_file is used to summary all the useful events
       into sp_test_time_info.dat.
    """
    list_total = []
    os.chdir(A.TIME_FILE_PATH)  # change to the directory of setup file.
    test = GlobalTest(0)
    each_file(A.TIME_FILE_PATH, list_total, test)
    # directory used to save processed data.
    result_file = A.DB_FILE_PATH_1 + 'sp_test_time_info.dat'
    # save list in corresponding file, to further data process.
    output = open(result_file, 'w')
    listdata_total = list(np.reshape(list_total, (test.n_files, 4)))
    output.write('name start_time stop_time duration\n')
    for i in range(test.n_files):  # read data in file
        for j in range(4):
            output.write(listdata_total[i][j]+' ')
        output.write('\n')
    output.close()


def init_time_data(conn, table01):
    """init_time_data is used to convert time file into table and
       initialize the time table.
    """
    c = get_cursor(conn)

    drop_table(conn, table01)
    create_table(conn, create_table01_sql)
    convert_time_info_into_file()
    os.chdir(A.DB_FILE_PATH_1)   # change directory back to origin_data
    file_open = open('sp_test_time_info.dat', 'r')
    i = 1
    for line in islice(file_open, 1, None):
        c.execute('insert into exp_time_data values(?, ?, ?, ?, ?)',
                  (i, line.split()[0], line.split()[1] + ' ' +
                   line.split()[2], line.split()[3] + ' ' + line.split()[4],
                   line.split()[5]))
        i = i + 1
    conn.commit()
    print("create database [{}] successfully!".format(table01))
