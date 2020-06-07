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
men_means = [0.658, 0.057, 0.284, 0.563]
# women_means = [25, 32, 34, 20]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means, width, label="Time offset 0s")
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
# autolabel(rects2)

fig.tight_layout()
fig.savefig("test.png", dpi=300, bbox_inches="tight")
plt.show()
