# -*- coding: utf-8 -*-
"""

@author: chenjianqi
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib.patches as patches
from process_program.process_program import *
from process_program.global_env.read import A
import numpy as np
import sqlite3
params = {"legend.fontsize": 10, "font.size": 20, "axes.titlesize": 16}
plt.rcParams.update(params)


class drawResultPlot7:
    def __init__(self, table13, table14, table15, table21, table22):
        self.table13 = table13
        self.table14 = table14
        self.table15 = table15
        self.table21 = table21
        self.table22 = table22

    def drawResultPlot(
        self, conn, table13, table14, table15, table21, table22
    ):

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
            "select * from [{}] where (guiding_coil_version = 0)  and
            guiding_coil_condition = 0 order by sf1_frequency asc".format(
                table21
            )
        ).fetchall()

        c.execute(
            "insert into [{}] select * from BM.[{}] where guiding_coil_version
            = 4 and sf2_position = 20".format(
                table22, table15
            )
        )
        c.execute(
            "insert into [{}] select * from BM.[{}] where BM.[{}].
            guiding_coil_version = 4 and BM.[{}].sf2_position = 20".format(
                table22, table13, table13, table13
            )
        )
        y1 = c.execute(
            "select * from [{}] where guiding_coil_version = 4 and
            guiding_coil_condition = 0 and measured_times = 1 and
            sf2_position = 20 order by sf2_frequency asc".format(
                table22
            )
        ).fetchall()

        #        y = c.execute("select * from [{}] where sf2_position = 30
        #       order by sf2_frequency asc".format(table22)).fetchall()
        # print(y1)
        conn.commit()
        c.execute("DETACH DATABASE 'BM'")

        fig, ax = plt.subplots()
        ax.set(
            xlabel="Frequency (kHz)",
            ylabel=r"$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$",
        )
        ax.set_title(
            r"$\bullet$ SF2 position: 20 cm above analysis foil", loc="left"
        )
        #        title=r'The result of SF1_OFF_SF2_ON_Tests with 
        #        coil version 4 position 25')
        #        ax.text(left,top)
        tick_spacing = 5
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.grid()
        #        print("y = [{}]".format(y))
        #        cs_lable = ['or','vr','^r','<r','>r','1r','2r','3r','4r',
        #                    'sr','pr','*r','hr','Hr','+r','xr']
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

        sf2_frequency_1 = []
        N_ucn_gadget_time_offset_0_1 = []
        N_ucn_gadget_time_offset_10_1 = []
        N_ucn_gadget_time_offset_20_1 = []
        N_ucn_Nanosc_1_time_offset_0_1 = []
        N_ucn_Nanosc_2_time_offset_0_1 = []
        N_ucn_Nanosc_1_time_offset_10_1 = []
        N_ucn_Nanosc_2_time_offset_10_1 = []
        N_ucn_Nanosc_1_time_offset_20_1 = []
        N_ucn_Nanosc_2_time_offset_20_1 = []
        N_ucn_norm_time_offset_0_1 = []
        N_ucn_norm_time_offset_10_1 = []
        N_ucn_norm_time_offset_20_1 = []

        #      calculate variable
        for i in range(len(y)):
            sf2_frequency.append(y[i][9])  # f2 frequency
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

        for i in range(len(y1)):
            sf2_frequency_1.append(y1[i][12])  # f2 frequency
            N_ucn_gadget_time_offset_0_1.append(y1[i][15])
            N_ucn_gadget_time_offset_10_1.append(y1[i][16])
            N_ucn_gadget_time_offset_20_1.append(y1[i][17])
            N_ucn_Nanosc_1_time_offset_0_1.append(y1[i][18])
            N_ucn_Nanosc_2_time_offset_0_1.append(y1[i][19])
            N_ucn_Nanosc_1_time_offset_10_1.append(y1[i][20])
            N_ucn_Nanosc_2_time_offset_10_1.append(y1[i][21])
            N_ucn_Nanosc_1_time_offset_20_1.append(y1[i][22])
            N_ucn_Nanosc_2_time_offset_20_1.append(y1[i][23])
            N_ucn_norm_time_offset_0_1.append(
                N_ucn_gadget_time_offset_0_1[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_0_1[i]
                    + N_ucn_Nanosc_2_time_offset_0_1[i]
                )
            )
            N_ucn_norm_time_offset_10_1.append(
                N_ucn_gadget_time_offset_10_1[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_10_1[i]
                    + N_ucn_Nanosc_2_time_offset_10_1[i]
                )
            )
            N_ucn_norm_time_offset_20_1.append(
                N_ucn_gadget_time_offset_20_1[i]
                * 1.0
                / (
                    N_ucn_Nanosc_1_time_offset_20_1[i]
                    + N_ucn_Nanosc_2_time_offset_20_1[i]
                )
            )

        #        print("N_ucn_norm_time_offset_0 = [{}]"
        #              .format(N_ucn_norm_time_offset_0))
        plt.plot(
            sf2_frequency,
            N_ucn_norm_time_offset_0,
            cs_label[0],
            label="SF1_ON_SF2_OFF GCV0",
            linestyle="-",
            linewidth=2.0,
        )
        plt.plot(
            sf2_frequency_1,
            N_ucn_norm_time_offset_0_1,
            cs_label[1],
            label="SF1_OFF_SF2_ON GCV4 with current off",
            linestyle="-",
            linewidth=2.0,
        )

        plt.legend()
        fig.savefig(
            A.DB_FILE_PATH_3
            + "\\pictures\\test_sf_state_condition_pos_20.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.show()


Obj_drawResultPlot7 = drawResultPlot7(
    A.TABLE_NAME_13,
    A.TABLE_NAME_14,
    A.TABLE_NAME_15,
    A.TABLE_NAME_21,
    A.TABLE_NAME_22,
)
