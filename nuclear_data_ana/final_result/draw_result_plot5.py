# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:51 2019

@author: chenjianqi
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = [
    "SF1_OFF_SF2_OFF",
    "SF1_ON_SF2_OFF",
    "SF1_OFF_SF2_ON",
    "SF1_ON_SF2_ON",
]
# men_means = [391215, 34207, 166935, 334693]

# position 20
# R_time_offset_0 = [0.658, 0.057, 0.284, 0.563]
# R_time_offset_10 = [0.733, 0.063, 0.312, 0.620]
# R_time_offset_20 = [0.773, 0.068, 0.344  , 0.663]

# position 25
# R_time_offset_0 = [0.659, 0.058 , 0.214, 0.596]
# R_time_offset_10 = [0.733, 0.063, 0.237, 0.664]
# R_time_offset_20 = [0.774, 0.068, 0.261, 0.703]

# position 30
R_time_offset_0 = [0.657, 0.058, 0.264, 0.577]
R_time_offset_10 = [0.722, 0.063, 0.297, 0.645]
R_time_offset_20 = [0.769, 0.068, 0.32, 0.683]


# women_means = [25, 32, 34, 20]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, R_time_offset_0, width, label="Time offset 0s")
rects2 = ax.bar(x, R_time_offset_10, width, label="Time offset 10s")
rects3 = ax.bar(x + width, R_time_offset_20, width, label="Time offset 20s")

# rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(r"$\mathregular{N_{Gadget}}$/$\mathregular{N_{Nanosc}}$")
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


fig.tight_layout()
fig.savefig("test.png", dpi=300, bbox_inches="tight")
plt.show()
