import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

from src.utils.logging_config import log


def plot_sorted_legend():
    handles, labels = plt.gca().get_legend_handles_labels()
    labels, handles = zip(*sorted(zip(labels, handles)))
    plt.legend(handles, labels)

def plt_with_disruption(plt_root, x, y, c='#2b2b2b', alpha=1.0,
                        label='_nolegend_', error_label='_nolegend_'):
    x = list(x)
    y = list(y)
    # Find the indices where there are gaps in x-values
    indices = np.where(np.diff(x) > 1)[0]

    # Plot line segments with dotted lines for connections
    start = 0
    for idx in indices:
        plt_root.plot(x[start:idx + 1], y[start:idx + 1], c=c, alpha=alpha, label=label)
        plt_root.plot([x[idx], x[idx + 1]], [y[idx], y[idx + 1]], c=c, alpha=alpha, linestyle='dotted',
                      label=error_label)

        error_label = '_nolegend_'
        label = '_nolegend_'
        start = idx + 1

    # Plot the remaining line segment
    plt_root.plot(x[start:], y[start:], c=c, alpha=alpha, label=label)


def plot_disruption_warning(ax):
    highlight_interval(ax, [1969, 1980], 'data\nunavailable')
    highlight_interval(ax, [1989, 2000], 'data\nunavailable')


def draw_hint(ax, position, text, horizontalalignment='center', verticalalignment='top'):
    padding = 2
    ax.scatter(position[0], position[1], marker='x', c='blue', s=50)
    ax.text(position[0], position[1] - padding, text,
            fontsize=12,
            color='black',
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment)


def highlight_interval(plt, interval, text, interval_color='#b8b5a7', text_vert_padding=3):
    plt.axvspan(interval[0], interval[1],
                label=text, color=interval_color, alpha=0.3)

    start = interval[0]
    end = interval[1]

    plt.text((start + end) / 2, plt.get_ylim()[0] + text_vert_padding, text, color='black',
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


def get_random_color():
    return random.choice([
        # '#2e492f',  # dark green
        # '#4d775b',  # light green
        # '#d9c5bb',  # eggshell
        # '#a74c20',  # dark orange
        # '#682f18',  # brown
        'green',
        'red',
        'blue',
        'yellow',
    ])
