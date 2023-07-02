import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.utils.logging_config import log

# TODO create custom color pallet etc.

def plt_with_disruption(plt_root, x, y, c='#2b2b2b', alpha=1.0, label=''):
    x = list(x)
    y = list(y)
    # Find the indices where there are gaps in x-values
    indices = np.where(np.diff(x) > 1)[0]

    # Plot line segments without connecting gaps
    start = 0
    for idx in indices:
        plt_root.plot(x[start:idx + 1], y[start:idx + 1], c=c, alpha=alpha, label=label)
        start = idx + 1

    # Plot the remaining line segment
    plt_root.plot(x[start:], y[start:], c=c, alpha=alpha)


def draw_hint(ax, position, text, horizontalalignment='center', verticalalignment='top'):
    padding = 2
    ax.scatter(position[0], position[1], marker='x', c='blue', s=50)
    ax.text(position[0], position[1] - padding, text,
            fontsize=12,
            color='black',
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment)


def highlight_interval(ax, interval, text, interval_color='#b8b5a7'):
    ax.axvspan(interval[0], interval[1],
               label=text, color=interval_color, alpha=0.3)

    start = interval[0]
    end = interval[1]

    # height = ax.get_ylim()
    # ax.plot([start, start], height, color='black', linestyle='dotted', linewidth=2, alpha=.5)
    # ax.plot([end, end], height, color='black', linestyle='dotted', linewidth=2, alpha=.5)

    ax.text((start + end) / 2, ax.get_ylim()[0] + 3, text, color='black',
            ha='center', va='bottom')


def draw_rectangle(block_dim):
    x_start = block_dim[0][0]
    x_end = block_dim[0][1]
    y_start = block_dim[1][0]
    y_end = block_dim[1][1]

    # rect = plt.Rectangle((x_start, y_start), x_end - x_start, y_end - y_start,
    #                      fill=True, facecolor='#f2f2f2', zorder=10, edgecolor='#dadada')
    rect = plt.Rectangle((x_start, y_start), x_end - x_start, y_end - y_start,
                         fill=True, facecolor='white', zorder=10, edgecolor='white')

    # get current axis instance
    ax = plt.gca()
    ax.add_patch(rect)
