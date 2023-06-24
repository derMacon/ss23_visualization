import matplotlib.pyplot as plt
import numpy as np
from ...utils.graph_utils import extract_win_stats



def v_score_count(df):
    df = df.sort_values(["v_score"])

    threshold = df['v_score'].quantile(0.99)
    df = df.drop(df[df['v_score'] > threshold].index)
    plt.hist2d(df['date_year'], df['v_score'])

    means_v_score = df.groupby(['date_year'])['v_score'].mean()
    plt.plot(means_v_score.keys(), means_v_score, color='red', label='mean')
    plt.title('visiting score')
    plt.legend()


def h_score_count(df):
    df = df.sort_values(["h_score"])

    threshold = df['h_score'].quantile(0.99)
    df = df.drop(df[df['h_score'] > threshold].index)
    plt.hist2d(df['date_year'], df['h_score'])

    means_h_score = df.groupby(['date_year'])['h_score'].mean()
    plt.plot(means_h_score.keys(), means_h_score, color='red', label='mean')
    plt.title('home score')
    plt.legend()


def vh_score_comparison(df):
    years = df.groupby(['date_year'])
    means_v_score = years['v_score'].mean()
    means_h_score = years['h_score'].mean()

    fig, ax = plt.subplots()

    # Plot the curves on the same graph
    ax.plot(means_v_score.keys(), means_v_score, label='visiting team score')
    ax.plot(means_h_score.keys(), means_h_score, label='home team score')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('compare score')
    ax.legend()


def winning_teams(df):
    overall_games_won_out = extract_win_stats(df)[2]
    # print(overall_games_won_out)

    fig, ax = plt.subplots()
    ax.set_title('wins per year')

    for curr_team, win_stats in overall_games_won_out.items():
        ax.plot(win_stats.keys(), win_stats.values(), label=curr_team)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        # ax.legend()