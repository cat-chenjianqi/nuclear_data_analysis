"""This module's docstring summary line.
re is used to convert string to bytes type. islice is used to avoid first line of flie.

os is used here to acquire file and path information.
"""
import os

import re
from itertools import islice

from process_program.global_env.read import A
from process_program.global_env.all_tables import create_table02_sql
from process_program.global_env.basic_fun import get_cursor, drop_table, create_table


def each_file(filepath, tran_result, final_result):
    """to find the .dat files that needs to be processed in directory.
    """
    n_files = 0
    path_dir = os.listdir(filepath)  # obtain the file name under current directory and return list
    for file_name in path_dir:
        # write the file name behind the current directory
        new_dir = os.path.join(filepath, file_name)
        if os.path.splitext(new_dir)[1] == ".dat":  # determine if it is dat file
            read_file(new_dir, tran_result, final_result)
            n_files = n_files+1


def read_file(filepath, tran_result, final_result):
    """to read each file and to filter the data that has the same name.
    """
    with open(filepath, "rb+") as file_bin:  # read in binary mode in order to read all contents.
        file_bin.seek(-2, os.SEEK_END)
        if file_bin.__next__() == str.encode('\n'):
            print("truncate works!")
            file_bin.seek(-2, os.SEEK_END)
            file_bin.truncate()
        # file_bin.truncate()
        file_bin.seek(0, 0)  # return back to the first line
        data1 = file_bin.readlines()  # read the whole file
        file_bin.close()
        for line in data1:
            line.strip(str.encode('\n'))  # convert str'\n' to bytes type
            data2 = line.split()
            str_to_byte = re.findall(str.encode('[0-9]'), data2[0])  # convert str to bytes type
            if str_to_byte:
                tran_result.append(line)
        len1 = int((len(tran_result))/3)
        for i in range(len1):
            final_result.append(tran_result[i]+tran_result[i+len1]+tran_result[i+2*len1])
        tran_result.clear()
        return final_result

def convert_det_file_into_table():
    """to summarize the data and meanwhile delete the redundant data(name).
    """
    tran_result = []
    final_result = []

    os.chdir(A.EVENT_FILE_PATH)
    each_file(A.EVENT_FILE_PATH, tran_result, final_result)
    result_file = A.DB_FILE_PATH_1+'sp_test_det_info.dat'  # the directory used to save data
    output = open(result_file, 'w')  # save list in corresponding file, to further data process.

    sql = 'name,\
    N_ucn_gadget_time_offset_0,\
    N_ucn_Nanosc_1_time_offset_0,\
    N_ucn_Nanosc_2_time_offset_0,\
    ratio_time_offset_0.\
    N_ucn_Gadget_time_offset_10,\
    N_ucn_Nanosc_1_time_offset_10,\
    N_ucn_Nanosc_2_time_offset_10,\
    ratio_time_offset_10,\
    N_ucn_Gadget_time_offset_20,\
    N_ucn_Nanosc_1_time_offset_20,\
    N_ucn_Nanosc_2_time_offset_20,\
    ratio_time_offset_20'
    output.write(sql+'\n')
    for line in final_result:
        line_str = bytes.decode(line)  # convert bytes to str
        data3 = line_str.split()
        data3.pop(5)  # delete the repeated name
        data3.pop(9)  # delete the repeated name
        str_line = str(data3).strip("[]")
        str_line = str_line.replace("_0001", "")
        str_line = str_line.replace("'", "")
        str_line = str_line.replace(",", "")
        # print(data3)
        output.write(str_line)
        output.write('\n')
    output.close()


def init_det_data(conn, table02):
    """to convert detector file into table.
    """
    c = get_cursor(conn)
    drop_table(conn, table02)
    create_table(conn, create_table02_sql)
    convert_det_file_into_table()
    os.chdir(A.DB_FILE_PATH_1)  # change directory back to origin_data
    file_open = open('sp_test_det_info.dat', 'r')
    i = 1
    for line in islice(file_open, 1, None):
        c.execute('insert into exp_det_data values(?, ?, ?, ?, ?, ?, ?, ?, ?,\
                                                  ?, ?, ?, ?, ?)',
                  (i, line.split()[0], line.split()[1], line.split()[2],
                   line.split()[3], line.split()[4], line.split()[5],
                   line.split()[6], line.split()[7], line.split()[8],
                   line.split()[9], line.split()[10], line.split()[11],
                   line.split()[12]))
        i = i + 1
    conn.commit()
    print("create database [{}] successfully!".format(table02))
