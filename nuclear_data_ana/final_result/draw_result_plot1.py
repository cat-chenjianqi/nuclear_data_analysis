# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from process_program.global_env.basic_fun import get_cursor
from process_program.global_env.read import A


class DrawResultPlot1:
    """
    """
    def __init__(self, table13, table14, table21):
        """
        """
        self.table13 = table13
        self.table14 = table14
        self.table21 = table21

    def draw_result_plot(self, conn, table13, table14, table21):
        """
        """
        c = get_cursor(conn)
        c.execute("""ATTACH [{}] as BM """.format(A.DB_FILE_2))
        c.execute("insert into [{}] select * from BM.[{}]"
                  .format(table21, table14))
        c.execute(
            "insert into [{}] select * from BM.[{}] where \
            BM.[{}].guiding_coil_version = 0"
            .format(table21, table13, table13)
        )
        data_con = c.execute(
            "select * from [{}] where (guiding_coil_version = 0)  and \
            guiding_coil_condition = 0 order by sf1_frequency asc" \
            .format(table21)
        ).fetchall()
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
        cs_label = ["or", "vb", "^g"]
        plt.xlim(0, 25)
        plt.ylim(0, 1)
        #      define variable
        sf1_frequency = []
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

        #      calculate variable
        for i in range(len(data_con)):
            sf1_frequency.append(data_con[i][9])  # unit of kHz
            num_ucn_gadget_time_offset_0.append(data_con[i][15])
            num_ucn_gadget_time_offset_10.append(data_con[i][16])
            num_ucn_gadget_time_offset_20.append(data_con[i][17])
            num_ucn_nanosc_1_time_offset_0.append(data_con[i][18])
            num_ucn_nanosc_2_time_offset_0.append(data_con[i][19])
            num_ucn_nanosc_1_time_offset_10.append(data_con[i][20])
            num_ucn_nanosc_2_time_offset_10.append(data_con[i][21])
            num_ucn_nanosc_1_time_offset_20.append(data_con[i][22])
            num_ucn_nanosc_2_time_offset_20.append(data_con[i][23])
            num_ucn_norm_time_offset_0.append(
                num_ucn_gadget_time_offset_0[i]
                * 1.0
                / (
                    num_ucn_nanosc_1_time_offset_0[i]
                    + num_ucn_nanosc_2_time_offset_0[i]
                )
            )
            num_ucn_norm_time_offset_10.append(
                num_ucn_gadget_time_offset_10[i]
                * 1.0
                / (
                    num_ucn_nanosc_1_time_offset_10[i]
                    + num_ucn_nanosc_2_time_offset_10[i]
                )
            )
            num_ucn_norm_time_offset_20.append(
                num_ucn_gadget_time_offset_20[i]
                * 1.0
                / (
                    num_ucn_nanosc_1_time_offset_20[i]
                    + num_ucn_nanosc_2_time_offset_20[i]
                )
            )
        plt.plot(
            sf1_frequency,
            num_ucn_norm_time_offset_0,
            cs_label[0],
            label="time_offset 0s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.plot(
            sf1_frequency,
            num_ucn_norm_time_offset_10,
            cs_label[1],
            label="time_offset 10s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.plot(
            sf1_frequency,
            num_ucn_norm_time_offset_20,
            cs_label[2],
            label="time_offset 20s",
            linestyle="-",
            linewidth=2.0,
        )
        plt.legend()
        fig.savefig(
            A.DB_FILE_PATH_3 + "\\pictures\\test.png", dpi=300, bbox_inches="tight"
        )
        plt.show()


Obj_drawResultPlot1 = DrawResultPlot1(A.TABLE_NAME_13, A.TABLE_NAME_14, A.TABLE_NAME_21)
