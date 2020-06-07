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
import math
params = {"legend.fontsize": 16, "font.size": 20, "axes.titlesize": 16}
plt.rcParams.update(params)


class drawResultPlot3:
    def __init__(self, table13, table15, table22):
        self.table13 = table13
        self.table15 = table15
        self.table22 = table22

    def drawResultPlot(self, conn, table13, table15, table22):

        cs_label = ["o", "v", "^"]
        cs_color = ["r", "b", "g"]
        # define variable
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
        Ucertainty_N_ucn_norm_time_offset_0 = []
        Ucertainty_N_ucn_norm_time_offset_10 = []
        Ucertainty_N_ucn_norm_time_offset_20 = []

        pos = ["20", "25"]
        fig, axs = plt.subplots(1, 2, sharey=True, figsize=(16, 9))
        #        fig, axs = plt.subplots(1,3, sharey=True, figsize=(4,3))

        for j in range(2):
            c = get_cursor(conn)
            c.execute("""ATTACH [{}] as BM """.format(A.DB_FILE_2))
            c.execute(
                "insert into [{}] select * from BM.[{}] where
                 guiding_coil_version = 4 and sf2_position = ?".format(
                    table22, table15
                ),
                (pos[j],),
            )
            c.execute(
                "insert into [{}] select * from BM.[{}] where BM.[{}]
                .guiding_coil_version = 4 and BM.[{}].sf2_position = ?".format(
                    table22, table13, table13, table13
                ),
                (pos[j],),
            )
            y = c.execute(
                "select * from [{}] where guiding_coil_version = 4 and
                guiding_coil_condition = 1 and measured_times = 1 and
                sf2_position = ? order by sf2_frequency asc".format(
                    table22
                ),
                (pos[j],),
            ).fetchall()
            c.execute("delete from [{}]".format(table22))
            conn.commit()
            c.execute("DETACH DATABASE 'BM'")

            #           calculate variable
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
                N_ucn_norm_time_offset_temp_0 = (
                    N_ucn_gadget_time_offset_0[i]
                    * 1.0
                    / (
                        N_ucn_Nanosc_1_time_offset_0[i]
                        + N_ucn_Nanosc_2_time_offset_0[i]
                    )
                )
                N_ucn_norm_time_offset_0.append(N_ucn_norm_time_offset_temp_0)
                Ucertainty_N_ucn_norm_time_offset_0.append(
                    N_ucn_norm_time_offset_temp_0
                    * math.sqrt(
                        1 / N_ucn_gadget_time_offset_0[i]
                        + 1
                        / (
                            N_ucn_Nanosc_1_time_offset_0[i]
                            + N_ucn_Nanosc_2_time_offset_0[i]
                        )
                    )
                )
                N_ucn_norm_time_offset_temp_10 = (
                    N_ucn_gadget_time_offset_10[i]
                    * 1.0
                    / (
                        N_ucn_Nanosc_1_time_offset_10[i]
                        + N_ucn_Nanosc_2_time_offset_10[i]
                    )
                )
                N_ucn_norm_time_offset_10.append(
                    N_ucn_norm_time_offset_temp_10
                )
                Ucertainty_N_ucn_norm_time_offset_10.append(
                    N_ucn_norm_time_offset_temp_10
                    * math.sqrt(
                        1 / N_ucn_gadget_time_offset_10[i]
                        + 1
                        / (
                            N_ucn_Nanosc_1_time_offset_10[i]
                            + N_ucn_Nanosc_2_time_offset_10[i]
                        )
                    )
                )
                N_ucn_norm_time_offset_temp_20 = (
                    N_ucn_gadget_time_offset_20[i]
                    * 1.0
                    / (
                        N_ucn_Nanosc_1_time_offset_20[i]
                        + N_ucn_Nanosc_2_time_offset_20[i]
                    )
                )
                N_ucn_norm_time_offset_20.append(
                    N_ucn_norm_time_offset_temp_20
                )
                Ucertainty_N_ucn_norm_time_offset_20.append(
                    N_ucn_norm_time_offset_temp_20
                    * math.sqrt(
                        1 / N_ucn_gadget_time_offset_20[i]
                        + 1
                        / (
                            N_ucn_Nanosc_1_time_offset_20[i]
                            + N_ucn_Nanosc_2_time_offset_20[i]
                        )
                    )
                )

            print(
                "Ucertainty_N_ucn_norm_time_offset_0 = [{}]".format(
                    Ucertainty_N_ucn_norm_time_offset_0
                )
            )
            # axs[j].plot(sf2_frequency,N_ucn_norm_time_offset_0,cs_label[0],
            # label = 'time_offset 0s',linestyle='-',linewidth=2.0)
            # axs[j].plot(sf2_frequency,N_ucn_norm_time_offset_10,cs_label[1],
            # label = 'time_offset 10s',linestyle='-',linewidth=2.0)
            # axs[j].plot(sf2_frequency,N_ucn_norm_time_offset_20,cs_label[2],
            # label = 'time_offset 20s',linestyle='-',linewidth=2.0)
            # axs[j].errorbar(sf2_frequency,N_ucn_norm_time_offset_0,xerr=0,
            # yerr=Ucertainty_N_ucn_norm_time_offset_0,marker=cs_label[0],
            # mfc=cs_color[0],label = 'time_offset 0s',linestyle='-',linewidth=2.0)
            # axs[j].errorbar(sf2_frequency,N_ucn_norm_time_offset_10,
            # xerr=0,yerr=Ucertainty_N_ucn_norm_time_offset_10,marker=cs_label[1],
            # mfc=cs_color[1],label = 'time_offset 10s',linestyle='-',linewidth=2.0)
            # axs[j].errorbar(sf2_frequency,N_ucn_norm_time_offset_20,xerr=0,
            # yerr=Ucertainty_N_ucn_norm_time_offset_20,marker=cs_label[2],
            # mfc=cs_color[2],label = 'time_offset 20s',linestyle='-',linewidth=2.0)
            axs[j].errorbar(
                sf2_frequency,
                N_ucn_norm_time_offset_0,
                xerr=0,
                yerr=Ucertainty_N_ucn_norm_time_offset_0,
                marker=cs_label[0],
                label="time_offset 0s",
                linestyle="-",
                linewidth=2.0,
            )
            axs[j].errorbar(
                sf2_frequency,
                N_ucn_norm_time_offset_10,
                xerr=0,
                yerr=Ucertainty_N_ucn_norm_time_offset_10,
                marker=cs_label[1],
                label="time_offset 10s",
                linestyle="-",
                linewidth=2.0,
            )
            axs[j].errorbar(
                sf2_frequency,
                N_ucn_norm_time_offset_20,
                xerr=0,
                yerr=Ucertainty_N_ucn_norm_time_offset_20,
                marker=cs_label[2],
                label="time_offset 20s",
                linestyle="-",
                linewidth=2.0,
            )
            axs[j].legend()
            axs[j].set_xlim(xmin=0, xmax=35)
            # axs[0].set_xlim(xmin=0,xmax=30)
            # axs[1].set_xlim(xmin=0,xmax=20)
            # axs[2].set_xlim(xmin=0,xmax=15)
            axs[j].set_ylim(ymin=0, ymax=1)
            axs[j].set(xlabel="Frequency (kHz)")
            axs[j].set(
                ylabel=r"$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$"
            )
            # axs[j].set(title=r'The result of SF1_OFF_SF2_ON_Tests with coil
            # version 4 position 25')
            # axs[j].set(xlabel='Frequency (kHz)', ylabel=
            # r'$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$')
            # axs[j].set_title(r'$\bullet$ Without guiding coil an
            # Position '+pos[j],loc = 'left')
            axs[j].set_title(r"$\bullet$ Position " + pos[j], loc="left")
            tick_spacing = 5
            axs[j].xaxis.set_major_locator(
                ticker.MultipleLocator(tick_spacing)
            )
            # xmajorLocator = MultipleLocator(5)
            # xmajorFormatter = FormatStrFormatter('%5.1f')
            # axs[j].xaxis.grid(True, which='major')
            axs[j].grid()

            sf2_frequency.clear()
            N_ucn_gadget_time_offset_0.clear()
            N_ucn_gadget_time_offset_10.clear()
            N_ucn_gadget_time_offset_20.clear()
            N_ucn_Nanosc_1_time_offset_0.clear()
            N_ucn_Nanosc_2_time_offset_0.clear()
            N_ucn_Nanosc_1_time_offset_10.clear()
            N_ucn_Nanosc_2_time_offset_10.clear()
            N_ucn_Nanosc_1_time_offset_20.clear()
            N_ucn_Nanosc_2_time_offset_20.clear()
            N_ucn_norm_time_offset_0.clear()
            N_ucn_norm_time_offset_10.clear()
            N_ucn_norm_time_offset_20.clear()
            Ucertainty_N_ucn_norm_time_offset_0.clear()
            Ucertainty_N_ucn_norm_time_offset_10.clear()
            Ucertainty_N_ucn_norm_time_offset_20.clear()

        fig.savefig(
            "test_sf1_off_sf2_on_without_gc.png", dpi=300, bbox_inches="tight"
        )
        plt.show()


Obj_drawResultPlot3 = drawResultPlot3(
    A.TABLE_NAME_13, A.TABLE_NAME_15, A.TABLE_NAME_22
)
