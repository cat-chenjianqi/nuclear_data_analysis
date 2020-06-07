#! G:\\python\\Hunter\\hunter python
# -*- coding: utf-8 -*-
# Author: Jianqi Chen
import sqlite3
import process_program.global_env.write
# from origin_data.convert_event_file_into_table import *
from origin_data.convert_time_file_into_table import *
# from origin_data.convert_basic_file_into_table import *
# from origin_data.convert_basic_event_time_file_into_origin import *
from process_program.global_env.read import A
from process_program.global_env.basic_fun import *
# from process_program.global_env import *
# from process_program.process_program import *
# from final_result.init_result_tables import *
# from final_result.drawResultPlot1 import *
# from final_result.drawResultPlot1_b import *
# from final_result.drawResultPlot2 import *
# from final_result.drawResultPlot3 import *
# from final_result.drawResultPlot7 import *
# from final_result.calc_sf_eff import *


def main():
    #    print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d
    #                                                       %H:%M:%S %A'))
    print('__name__ value: ', __name__)
# ---- initialization --------------------------------------------------------#

    conn = get_conn(A.DB_FILE_1)
    init_time_data(conn, A.TABLE_NAME_01)
    # init_det_data(conn, A.TABLE_NAME_02)
#    init_basic_data(conn, A.TABLE_NAME_03)
#    init_origin_data(conn, A.TABLE_NAME_01, A.TABLE_NAME_02, A.TABLE_NAME_03,
#                     A.TABLE_NAME_04)
# --- procession ---------------------------------------------------------- -#

    # conn = get_conn(A.DB_FILE_2)
    # process_program(conn, A.TABLE_NAME_04, A.TABLE_NAME_11, A.TABLE_NAME_12,
                    # A.TABLE_NAME_13, A.TABLE_NAME_14, A.TABLE_NAME_15,
                    # A.TABLE_NAME_16)
# --- Draw ------------------------------------------------------------------#

    # conn = get_conn(A.DB_FILE_3)
    # init_result_tables(conn, A.TABLE_NAME_21, A.TABLE_NAME_22, A.TABLE_NAME_23)

#   calculate sf efficiency
    # conn = get_conn(A.DB_FILE_3)
    # Obj_calc_sf_eff.calc_sf_eff(conn,A.TABLE_NAME_12,A.TABLE_NAME_23)

#   draw the SF1_ON_SF2_OFF test
    # conn = get_conn(A.DB_FILE_3)
    # Obj_drawResultPlot1.drawResultPlot(conn,A.TABLE_NAME_13,A.TABLE_NAME_14,
    #                                    A.TABLE_NAME_21)

#   draw the SF1_ON_SF2_OFF test
    # conn = get_conn(A.DB_FILE_3)
    # Obj_drawResultPlot1_b.drawResultPlot(conn,A.TABLE_NAME_13,A.TABLE_NAME_14,
    #                                      A.TABLE_NAME_21)

#   draw the SF1_OFF_SF2_ON at position 20
    # conn = get_conn(A.DB_FILE_3)
    # Obj_drawResultPlot2.drawResultPlot(conn,A.TABLE_NAME_13,A.TABLE_NAME_15,
    #                                    A.TABLE_NAME_22)

#   draw the SF at different state
    # conn = get_conn(A.DB_FILE_3)
    # Obj_drawResultPlot7.drawResultPlot(conn,A.TABLE_NAME_13,A.TABLE_NAME_14,
    #                                    A.TABLE_NAME_15,A.TABLE_NAME_21,
    #                                    A.TABLE_NAME_22)

if __name__ == '__main__':
    main()

    # conn = get_conn(A.DB_FILE_3)
    # c=get_cursor(conn)
    # y = c.execute('select * from sqlite_master where type="table" order
    # by name')
    # for x in y:
    # print(x)
