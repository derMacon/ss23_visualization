import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from src.utils.processing_utils import extract_game_count
from src.utils.styling_utils import *
from src.utils.logging_config import log


def attendance_per_year(df):
    df = df[df['attendance'].notna()]

    means_v_score = df.groupby(['date_year'])['attendance'].mean().to_dict()
    # means_v_score = {str(key): value for key, value in means_v_score.items()}

    x_vals = list(means_v_score.keys())
    # plt.plot(x_vals, means_v_score.values(), color='red', label='mean')
    plt_with_disruption(plt, x_vals, means_v_score.values(), c='red', label='mean')

    # plt.xticks(x_vals[::5]) # only display every nth value on the x axis
    # decades = sorted(df['date_decade'].unique())[1::2]
    # plt.xticks(np.linspace(0, len(x_vals) - 1, len(decades)), decades)  # Spread labels evenly

    plt.title('attendance')
    plt.legend()


def data_per_year(df):
    data_per_year = df.groupby(['date_year']).size().to_dict()

    fig, ax = plt.subplots()
    plt_with_disruption(ax, data_per_year.keys(), data_per_year.values(), label='data rows per year')
    ax.set_xlabel('decade')
    ax.set_ylabel('entries per year')

    plt.title("Available Data")
    plt.legend()


def games_per_year_overall(df):
    data = extract_game_count(df)['games_per_year_overall']
    log.debug('games_per_year: %s', data)
    # plt.plot(list(data.keys()), list(data.values()))

    fig, ax = plt.subplots()
    plt_with_disruption(ax, list(data.keys()), list(data.values()))
    plot_disruption_warning()

def check_neighbors(array):
    array = list(array)
    for i in range(1, len(array)):
        if abs(array[i] - array[i-1]) != 1:
            return False
    return True

def games_per_year_per_team(df):
    data = extract_game_count(df)
    games_per_year_per_team = data['games_per_year_per_team']
    log.debug('games_per_year_per_team: %s', games_per_year_per_team)

    fig, ax = plt.subplots(figsize=(12, 6))
    for curr_team, count_per_year in games_per_year_per_team.items():
        plt_with_disruption(ax, count_per_year.keys(), count_per_year.values(), c=cm.gray(0.7), alpha=0.2, label=curr_team)

    games_per_year_avg = data['games_per_year_avg']
    log.debug('games_per_year_overall: %s', data)
    log.debug('games_per_year_avg: %s', games_per_year_avg)

    plt_with_disruption(ax, games_per_year_avg.keys(), games_per_year_avg.values())

    draw_hint(ax, [1903, count_per_year[1903]], 'new league')
    highlight_interval(ax, [1914, 1918], 'WW1')
    highlight_interval(ax, [1939, 1945], 'WW2')
    highlight_interval(ax, [1969, 1980], 'data\nunavailable', text_vert_padding=7)
    highlight_interval(ax, [1989, 2000], 'data\nunavailable')
    draw_hint(ax, [1960, games_per_year_avg[1960]], 'league\nexpansion')
    draw_hint(ax, [1981, games_per_year_avg[1981]], 'strike')

    plt.title('Average Games Played Per Year')
    plt.xlabel('games played')
    plt.ylabel('decade')
