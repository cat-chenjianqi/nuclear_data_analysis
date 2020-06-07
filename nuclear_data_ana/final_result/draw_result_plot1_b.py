# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
from process_program.process_program import *
from process_program.global_env.read import A
import numpy as np
import sqlite3
params = {"legend.fontsize": 10, "font.size": 20, "axes.titlesize": 16}
plt.rcParams.update(params)


class drawResultPlot1_b:
    def __init__(self, table13, table14, table21):
        self.table13 = table13
        self.table14 = table14
        self.table21 = table21

    def drawResultPlot(self, conn, table13, table14, table21):

        c = get_cursor(conn)
        c.execute("""ATTACH [{}] as BM """.format(A.DB_FILE_2))
        c.execute(
            "insert into [{}] select * from BM.[{}]".format(table21, table14)
        )
        c.execute(
            "insert into [{}] select * from BM.[{}] where BM.[{}]
            .guiding_coil_version = 0".format(
                table21, table13, table13
            )
        )
        y = c.execute(
            "select * from [{}] where id = 5 or id = 9 or id = 13 or id = 34 or
            id = 116".format(
                table21
            )
        ).fetchall()
        # y = c.execute("select * from [{}] where (guiding_coil_version = 0 or
        # guiding_coil_version = 4)  and guiding_coil_condition = 0 order by
        # sf1_frequency asc".format(table21)).fetchall()
        print(y)
        conn.commit()
        c.execute("DETACH DATABASE 'BM'")

        fig, ax = plt.subplots()
        ax.set(
            xlabel="Frequency (kHz)",
            ylabel=r"$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$",
            title=r"",
        )
        ax.grid()
        #        print("y = [{}]".format(y))
        # cs_label = ['or','vb','^g']
        cs_label = ["or", "vb", "^g", ">c", "<y"]
        label = [
            "Without_GC",
            "GC_v1_Current_on",
            "GC_v2_Current_on",
            "GC_v4_Current_on",
            "GC_v4_Current_off",
        ]
        plt.xlim(0, 25)
        plt.ylim(0, 0.2)
        #      define variable
        sf1_frequency = []
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
            sf1_frequency.append(y[i][9])  # unit of kHz
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
            #        print("N_ucn_norm_time_offset_0 = [{}]"
            #              .format(N_ucn_norm_time_offset_0))
            plt.plot(
                sf1_frequency[i],
                N_ucn_norm_time_offset_0[i],
                cs_label[i],
                label=label[i],
            )
            plt.legend(loc="upper left")

        fig.savefig(
            A.DB_FILE_PATH_3 + "\\pictures\\test.png",
            dpi=300,
            bbox_inches="tight",
        )
        #        fig.savefig("test.png",dpi=300)
        plt.show()


Obj_drawResultPlot1_b = drawResultPlot1_b(
    A.TABLE_NAME_13, A.TABLE_NAME_14, A.TABLE_NAME_21
)
