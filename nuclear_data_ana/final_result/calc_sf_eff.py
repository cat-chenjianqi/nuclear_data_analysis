# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import math
import numpy as np

from process_program.global_env.read import A
from process_program.global_env.basic_fun import get_cursor

class CalcSfEff:
    def __init__(self, table12, table23):
        self.table12 = table12
        self.table23 = table23

    def calc_sf_eff(self, conn, table12, table23):

        c = get_cursor(conn)
        c.execute("""ATTACH [{}] as BM """.format(A.DB_FILE_2))
        # start from file NY_SF1_OFF_15kHz_SF2_OFF_13kHz_25cm_withoutGCv4_bis
        c.execute(
            "insert into [{}] select * from BM.[{}] limit 24 offset 90".format(
                table23, table12
            )
        )
        y = c.execute("select * from [{}]".format(table23)).fetchall()
        conn.commit()
        c.execute("DETACH DATABASE 'BM'")

        sf2_frequency = []
        num_ucn_gadget_time_offset_0 = []
        num_ucn_gadget_time_offset_10 = []
        num_ucn_gadget_time_offset_20 = []
        num_ucn_nanosc_1_time_offset_0 = []
        num_ucn_nanosc_2_time_offset_0 = []
        num_ucn_nanosc_1_time_offset_10 = []
        num_ucn_nanosc_2_time_offset_10 = []
        num_ucn_nanosc_1_time_offset_20 = []
        num_ucn_nanosc_2_time_offset_20 = []
        num_ucn_norm_time_offset_0 = []
        num_ucn_norm_time_offset_10 = []
        num_ucn_norm_time_offset_20 = []
        uncertainty_num_ucn_norm_time_offset_0 = []
        uncertainty_num_ucn_norm_time_offset_10 = []
        uncertainty_num_ucn_norm_time_offset_20 = []
        uncertainty_listdata_total_0 = []
        uncertainty_listdata_total_10 = []
        uncertainty_listdata_total_20 = []
        run_time = []
        #      calculate variable
        for i in range(len(y)):
            print(y[i][1], " ", y[i][15], " ", y[i][16], " ", y[i][17])
            sf2_frequency.append(y[i][12])  # f2 frequency
            num_ucn_gadget_time_offset_0.append(y[i][15])
            num_ucn_gadget_time_offset_10.append(y[i][16])
            num_ucn_gadget_time_offset_20.append(y[i][17])
            num_ucn_nanosc_1_time_offset_0.append(y[i][18])
            num_ucn_nanosc_2_time_offset_0.append(y[i][19])
            num_ucn_nanosc_1_time_offset_10.append(y[i][20])
            num_ucn_nanosc_2_time_offset_10.append(y[i][21])
            num_ucn_nanosc_1_time_offset_20.append(y[i][22])
            num_ucn_nanosc_2_time_offset_20.append(y[i][23])
            run_time.append(y[i][26])

            num_ucn_norm_time_offset_temp_0 = num_ucn_gadget_time_offset_0[i] / (
                num_ucn_nanosc_1_time_offset_0[i] + num_ucn_nanosc_2_time_offset_0[i]
            )
            num_ucn_norm_time_offset_0.append(num_ucn_norm_time_offset_temp_0)
            uncertainty_num_ucn_norm_time_offset_0.append(
                math.sqrt(num_ucn_norm_time_offset_temp_0)
            )

            num_ucn_norm_time_offset_temp_10 = num_ucn_gadget_time_offset_10[i] / (
                num_ucn_nanosc_1_time_offset_10[i] + num_ucn_nanosc_2_time_offset_10[i]
            )
            num_ucn_norm_time_offset_10.append(num_ucn_norm_time_offset_temp_10)
            uncertainty_num_ucn_norm_time_offset_10.append(
                math.sqrt(num_ucn_norm_time_offset_temp_10)
            )

            num_ucn_norm_time_offset_temp_20 = num_ucn_gadget_time_offset_20[i] / (
                num_ucn_nanosc_1_time_offset_20[i] + num_ucn_nanosc_2_time_offset_20[i]
            )
            num_ucn_norm_time_offset_20.append(num_ucn_norm_time_offset_temp_20)
            uncertainty_num_ucn_norm_time_offset_20.append(
                math.sqrt(num_ucn_norm_time_offset_temp_20)
            )

        listdata_total_0 = list(np.reshape(num_ucn_norm_time_offset_0, (6, 4)))
        listdata_total_10 = list(np.reshape(num_ucn_norm_time_offset_10, (6, 4)))
        listdata_total_20 = list(np.reshape(num_ucn_norm_time_offset_20, (6, 4)))
        print(
            listdata_total_0,
            "\n\n",
            listdata_total_10,
            "\n\n",
            listdata_total_20,
            "\n\n",
        )

        uncertainty_listdata_total_0 = list(
            np.reshape(uncertainty_num_ucn_norm_time_offset_0, (6, 4))
        )
        uncertainty_listdata_total_10 = list(
            np.reshape(uncertainty_num_ucn_norm_time_offset_10, (6, 4))
        )
        uncertainty_listdata_total_20 = list(
            np.reshape(uncertainty_num_ucn_norm_time_offset_20, (6, 4))
        )
        sf_eff_formula(listdata_total_0, uncertainty_listdata_total_0)


    def sf_eff_formula(listdata_total_0, uncertainty_listdata_total_0):

        f_offset_0 = np.empty((len(listdata_total_0), 4), dtype=float)
        f_offset_10 = np.empty((len(listdata_total_10), 4), dtype=float)
        f_offset_20 = np.empty((len(listdata_total_20), 4), dtype=float)

        for i in range(1, len(listdata_total_0) + 1):
            f_offset_0[i - 1][0] = (
                (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][1])
                * 100
                / (listdata_total_0[i-1][0]-listdata_total_0[i-1][2])
            )
            f_offset_0[i - 1][1] = f_offset_0[i - 1][2] * math.sqrt(
                (
                    uncertainty_listdata_total_0[i - 1][0]
                    / (listdata_total_0[i - 1][0] - listdata_total_0[i - 1][2])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][2]
                    / (listdata_total_0[i - 1][0] - listdata_total_0[i - 1][2])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][3]
                    / (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][1])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][1]
                    / (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][1])
                )
                ** 2
            )

            f_offset_0[i - 1][2] = (
                (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][2])
                * 100
                / (listdata_total_0[i - 1][0] - listdata_total_0[i - 1][1])
            )
            f_offset_0[i - 1][3] = f_offset_0[i - 1][0] * math.sqrt(
                (
                    uncertainty_listdata_total_0[i - 1][0]
                    / (listdata_total_0[i - 1][0] - listdata_total_0[i - 1][1])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][1]
                    / (listdata_total_0[i - 1][0] - listdata_total_0[i - 1][1])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][2]
                    / (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][2])
                )
                ** 2
                + (
                    uncertainty_listdata_total_0[i - 1][3]
                    / (listdata_total_0[i - 1][3] - listdata_total_0[i - 1][2])
                )
                ** 2
            )
        print(f_offset_0, "\n\n")

Obj_calc_sf_eff = CalcSfEff(A.TABLE_NAME_12, A.TABLE_NAME_23)
