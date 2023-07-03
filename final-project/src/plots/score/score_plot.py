import matplotlib.pyplot as plt
import random
import pprint
import numpy as np
from matplotlib import cm

from src.utils.datastructure_utils import *
from src.utils.processing_utils import *
from src.utils.styling_utils import *

from src.utils.logging_config import log


def v_score_count(df):
    df = df.sort_values(["v_score"])

    threshold = df['v_score'].quantile(0.99)
    df = df.drop(df[df['v_score'] > threshold].index)
    fig, ax = plt.subplots()
    ax.hist2d(df['date_year'], df['v_score'], bins=[20, 15])

    means_v_score = df.groupby(['date_year'])['v_score'].mean()
    plt_with_disruption(ax, means_v_score.keys(), means_v_score, c='red', label='mean')
    # plt.plot(means_v_score.keys(), means_v_score, color='red', label='mean')

    ax.set_ylabel('score')
    ax.set_xlabel('decade')
    plt.title('Visiting Score')
    plt.legend()


def h_score_count(df):
    df = df.sort_values(["h_score"])

    threshold = df['h_score'].quantile(0.99)
    df = df.drop(df[df['h_score'] > threshold].index)

    fig, ax = plt.subplots()
    ax.hist2d(df['date_year'], df['h_score'], bins=[20, 15])

    means_h_score = df.groupby(['date_year'])['h_score'].mean()
    plt_with_disruption(ax, means_h_score.keys(), means_h_score, c='red', label='mean')

    ax.set_ylabel('score')
    ax.set_xlabel('decade')
    plt.title('Home Score')
    plt.legend()


def vh_score_comparison(df):
    years = df.groupby(['date_year'])
    means_v_score = years['v_score'].mean()
    means_h_score = years['h_score'].mean()

    fig, ax = plt.subplots()

    # Plot the curves on the same graph
    plt_with_disruption(ax, means_v_score.keys(), means_v_score, c='#c95604', label='mean - visiting team score')
    plt_with_disruption(ax, means_h_score.keys(), means_h_score, c='#3904c9', label='mean - home team score')

    ax.set_xlabel('decade')
    ax.set_ylabel('score')
    ax.set_title('Home / Visiting Score Comparison')
    ax.legend()


def winning_teams(df):
    bug = df[df['v_name_translate'] == 'Washington - Nationals']
    bug2 = df[df['h_name_translate'] == 'Washington - Nationals']

    win_stats = extract_win_stats(df)
    # win_avg = calc_win_averages(df)

    # home_games_won_per_year = win_stats['home_games_won_per_year']
    # home_games_won_total = win_stats['home_games_won_total']
    # visiting_games_won_per_year = win_stats['visiting_games_won_per_year']
    # visiting_games_won_total = win_stats['visiting_games_won_total']
    overall_games_won_per_year = win_stats['overall_games_won_per_year']
    overall_games_won_total = win_stats['overall_games_won_total']

    # win_avg_per_year_per_team = win_avg['win_avg_per_year_per_team']
    # win_avg_total_per_team = win_avg['win_avg_total_per_team']
    # visiting_games_win_avg_per_year_per_team = win_avg['visiting_games_win_avg_per_year_per_team']
    # home_games_win_avg_per_year_per_team = win_avg['home_games_win_avg_per_year_per_team']

    max_total_team = max(overall_games_won_total, key=overall_games_won_total.get)
    min_total_team = min(overall_games_won_total, key=overall_games_won_total.get)

    worst_score_yearly = 100000
    worst_team_yearly = ''
    worst_year = 0

    best_score_yearly = 100000
    best_team_yearly = ''
    best_year = 0

    for curr_team, win_count_per_year in overall_games_won_per_year.items():

        curr_worst_year = min(win_count_per_year, key=win_count_per_year.get)
        curr_worst_score = win_count_per_year[curr_worst_year]
        if curr_worst_score < worst_score_yearly:
            worst_team_yearly = curr_team
            worst_score_yearly = curr_worst_score
            worst_year = curr_worst_year

        curr_best_year = max(win_count_per_year, key=win_count_per_year.get)
        curr_best_score = win_count_per_year[curr_best_year]
        if curr_best_score < best_score_yearly:
            best_team_yearly = curr_team
            best_score_yearly = curr_best_score
            best_year = curr_best_year

    highlighted_teams = {
        max_total_team: "total - most wins: %s - %s" % (max_total_team, overall_games_won_total[max_total_team]),
        min_total_team: "total - least wins: %s - %s" % (min_total_team, overall_games_won_total[min_total_team]),
        best_team_yearly: "most wins in one year: %s, %s - %s" % (best_team_yearly, best_year, best_score_yearly),
        worst_team_yearly: "least wins in one year: %s, %s - %s" % (worst_team_yearly, worst_year, worst_score_yearly),
    }

    log.debug('highlighted_teams: %s', highlighted_teams)
    log.debug('win_stats: %s', pprint.pformat(win_stats))

    fig, ax = plt.subplots()
    # ax.set_title('Wins Per Year')
    for curr_team, win_stats in overall_games_won_per_year.items():
        if curr_team in highlighted_teams:
            # ax.plot(win_stats.keys(), win_stats.values(), label=highlighted_teams[curr_team])
            plt_with_disruption(ax, win_stats.keys(), win_stats.values(),
                                c=get_random_color(), label=highlighted_teams[curr_team], error_label='_nolegend_')
        else:
            # ax.plot(win_stats.keys(), win_stats.values(), c=cm.gray(0.8), alpha=0.2, zorder=-1)
            plt_with_disruption(ax, win_stats.keys(), win_stats.values(),
                                c=cm.gray(0.8), alpha=0.2, error_label='_nolegend_')

    plt.title('Wins Per Year')
    ax.set_ylabel('wins')
    ax.set_xlabel('decade')
    plt.legend()


def win_ratio_teams(df):
    win_ratio_per_year = extract_win_stats(df)[2:5]
