import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# TODO create custom color pallet etc.

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
