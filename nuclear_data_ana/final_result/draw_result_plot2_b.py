# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from process_program.process_program import *
from process_program.global_env.read import A
import numpy as np
import sqlite3


class drawResultPlot2:
    def __init__(self, table13, table15, table22):
        self.table13 = table13
        self.table15 = table15
        self.table22 = table22

    def drawResultPlot(self, conn, table13, table15, table22):

        c = get_cursor(conn)
        c.execute("""ATTACH [{}] as BM """.format(A.DB_FILE_2))
        c.execute(
            "insert into [{}] select * from BM.[{}] where guiding_coil_version 
            = 4 and sf2_position = 20".format(
                table22, table15
            )
        )
        c.execute(
            "insert into [{}] select * from BM.[{}] where BM.[{}]
            .guiding_coil_version = 4 and BM.[{}].sf2_position = 20".format(
                table22, table13, table13, table13
            )
        )
        y = c.execute(
            "select * from [{}] where guiding_coil_version = 4 and 
            guiding_coil_condition = 0 and measured_times = 1 and
            sf2_position = 20 order by sf2_frequency asc".format(
                table22
            )
        ).fetchall()
        #        y = c.execute("select * from [{}] where sf2_position
        #          = 30 order by sf2_frequency asc".format(table22)).fetchall()
        #        print(y)
        conn.commit()
        c.execute("DETACH DATABASE 'BM'")

        fig, ax = plt.subplots()
        ax.set(
            xlabel="Frequency (kHz)",
            ylabel=r"$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$",
        )
        ax.set_title(
            r"$\bullet$ Without guiding coil and Position 20", loc="left"
        )
        # title=r'The result of SF1_OFF_SF2_ON_Tests with coil version 4
        # position 25')
        # ax.text(left,top)
        ax.grid()
        # print("y = [{}]".format(y))
        # cs_lable = ['or','vr','^r','<r','>r','1r','2r','3r','4r',
        # 'sr','pr','*r','hr','Hr','+r','xr']
        cs_label = ["or", "vb", "^g"]
        plt.xlim(0, 30)
        plt.ylim(0, 1)
        #      define variable
        sf2_frequency = []
        N_ucn_gadget_time_offset_0 = []
        N_ucn_gadget_time_offset_10 = []
        N_ucn_gadget_time_offset_20 = []
        N_ucn_Nanosc_1_time_offset_0 = []
        N_ucn_Nanosc_2_time_offset_0 = []
        N_ucn_Nanosc_1_time_offset_10 = []
        N_ucn_Nanosc_2_time_offset_10 = []
        N_ucn_Nanosc_1_time_offset_20 = []
        N_ucn_Nanosc_2_time_offset_20 = []
        N_ucn_norm_time_offset_0 = []
        N_ucn_norm_time_offset_10 = []
        N_ucn_norm_time_offset_20 = []
        #      calculate variable
        for i in range(len(y)):
            sf2_frequency.append(y[i][12])  # f2 frequency
            N_ucn_gadget_time_offset_0.append(y[i][15])
            N_ucn_gadget_time_offset_10.append(y[i][16])
            N_ucn_gadget_time_offset_20.append(y[i][17])
            N_ucn_Nanosc_1_time_offset_0.append(y[i][18])
            N_ucn_Nanosc_2_time_offset_0.append(y[i][19])
            N_ucn_Nanosc_1_time_offset_10.append(y[i][20])
            N_ucn_Nanosc_2_time_offset_10.append(y[i][21])
            N_ucn_Nanosc_1_time_offset_20.append(y[i][22])
            N_ucn_Nanosc_2_time_offset_20.append(y[i][23])
            N_ucn_norm_time_offset_0.append(
                N_ucn_gadget_time_offset_0[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_0[i]
                    + N_ucn_Nanosc_2_time_offset_0[i]
                )
            )
            N_ucn_norm_time_offset_10.append(
                N_ucn_gadget_time_offset_10[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_10[i]
                    + N_ucn_Nanosc_2_time_offset_10[i]
                )
            )
            N_ucn_norm_time_offset_20.append(
                N_ucn_gadget_time_offset_20[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_20[i]
                    + N_ucn_Nanosc_2_time_offset_20[i]
                )
            )
        # print("N_ucn_norm_time_offset_0 = [{}]".format(N_ucn_norm_time_offset_0))
        plt.plot(
            sf2_frequency,
            N_ucn_norm_time_offset_0,
            cs_label[0],
            label="time_offset 0s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.plot(
            sf2_frequency,
            N_ucn_norm_time_offset_10,
            cs_label[1],
            label="time_offset 10s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.plot(
            sf2_frequency,
            N_ucn_norm_time_offset_20,
            cs_label[2],
            label="time_offset 20s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.legend()
        fig.savefig("SF1_OFF_SF2_ON_POS_20_WO_GC_test.png")
        plt.show()


Obj_drawResultPlot2 = drawResultPlot2(
    A.TABLE_NAME_13, A.TABLE_NAME_15, A.TABLE_NAME_22
)
