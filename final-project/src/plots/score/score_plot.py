import pprint

from matplotlib import cm

from src.utils.logging_config import log
from src.utils.processing_utils import *
from src.utils.styling_utils import *


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
    plot_sorted_legend()


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
    plot_sorted_legend()


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
    win_stats = extract_win_stats(df)

    overall_games_won_per_year = win_stats['overall_games_won_per_year']
    overall_games_won_total = win_stats['overall_games_won_total']

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
        "total - most wins: %s - %s" % (max_total_team, overall_games_won_total[max_total_team]): max_total_team,
        "total - least wins: %s - %s" % (min_total_team, overall_games_won_total[min_total_team]): min_total_team,
        "most wins in one year: %s, %s - %s" % (best_team_yearly, best_year, best_score_yearly): best_team_yearly,
        "least wins in one year: %s, %s - %s" % (worst_team_yearly, worst_year, worst_score_yearly): worst_team_yearly,
    }

    log.debug('highlighted_teams: %s', highlighted_teams)
    log.debug('win_stats: %s', pprint.pformat(win_stats))

    fig, ax = plt.subplots(figsize=(10, 5))
    for curr_team, win_stats in overall_games_won_per_year.items():
        plt_with_disruption(ax, win_stats.keys(), win_stats.values(),
                            c=cm.gray(0.8), alpha=0.2, error_label='_nolegend_')

    colors = iter(['red', 'green', 'purple', 'blue'])
    for curr_descr, curr_team in highlighted_teams.items():
        # ax.plot(win_stats.keys(), win_stats.values(), label=highlighted_teams[curr_team])
        curr_win_stats = overall_games_won_per_year[curr_team]
        plt_with_disruption(ax, curr_win_stats.keys(), curr_win_stats.values(),
                            c=next(colors), label=curr_descr)

    plt.title('Wins Per Year')
    plt.ylim(0, 140)
    ax.set_ylabel('wins')
    ax.set_xlabel('decade')
    plot_sorted_legend()


def win_ratio_teams(df):
    win_averages = calc_win_averages(df)
    win_avg_per_year_per_team = win_averages['win_avg_per_year_per_team']

    win_avg_total_per_team = win_averages['win_avg_total_per_team']

    max_total_team = max(win_avg_total_per_team, key=win_avg_total_per_team.get)
    min_total_team = min(win_avg_total_per_team, key=win_avg_total_per_team.get)

    worst_avg_yearly = 1
    worst_team_yearly = ''
    worst_year = 0

    best_avg_yearly = 0
    best_team_yearly = ''
    best_year = 0

    for curr_team, win_avg_per_year in win_avg_per_year_per_team.items():

        curr_worst_year = min(win_avg_per_year, key=win_avg_per_year.get)
        curr_worst_score = win_avg_per_year[curr_worst_year]
        if curr_worst_score < worst_avg_yearly:
            worst_team_yearly = curr_team
            worst_avg_yearly = curr_worst_score
            worst_year = curr_worst_year

        curr_best_year = max(win_avg_per_year, key=win_avg_per_year.get)
        curr_best_score = win_avg_per_year[curr_best_year]
        if curr_best_score > best_avg_yearly:
            best_team_yearly = curr_team
            best_avg_yearly = curr_best_score
            best_year = curr_best_year

    highlighted_teams = {
        "best average over all time: %s - %.2f" % (
            max_total_team, win_avg_total_per_team[max_total_team]): max_total_team,
        "worst average over all time: %s - %.2f" % (
            min_total_team, win_avg_total_per_team[min_total_team]): min_total_team,
        "best average in one year: %s, %s - %.2f" % (best_team_yearly, best_year, best_avg_yearly): best_team_yearly,
        "worst average in one year: %s, %s - %.2f" % (
            worst_team_yearly, worst_year, worst_avg_yearly): worst_team_yearly,
    }

    fig, ax = plt.subplots(figsize=(10, 5))
    for curr_team, curr_stats in win_avg_per_year_per_team.items():
        plt_with_disruption(ax, list(curr_stats.keys()), list(curr_stats.values()),
                            c=cm.gray(0.8), alpha=0.2, label='_nolegend_')

    colors = iter(['red', 'green', 'purple', 'blue'])
    for curr_descr, curr_team in highlighted_teams.items():
        curr_team_stats = win_avg_per_year_per_team[curr_team]
        plt_with_disruption(ax, curr_team_stats.keys(), curr_team_stats.values(),
                            c=next(colors), label=curr_descr)

    plt.xlabel('decade')
    plt.ylabel('win average per team')
    plt.title('Win Average Per Team')
    plt.ylim((0.2, 0.9))
    plt.legend()


def home_win_avg(df):
    win_averages = calc_win_averages(df)
    home_games_win_avg_per_year_per_team = win_averages['home_games_win_avg_per_year_per_team']


    worst_avg_yearly = 1
    worst_team_yearly = ''
    worst_year = 0

    best_avg_yearly = 0
    best_team_yearly = ''
    best_year = 0

    for curr_team, win_avg_per_year in home_games_win_avg_per_year_per_team.items():

        curr_worst_year = min(win_avg_per_year, key=win_avg_per_year.get)
        curr_worst_score = win_avg_per_year[curr_worst_year]
        if curr_worst_score < worst_avg_yearly:
            worst_team_yearly = curr_team
            worst_avg_yearly = curr_worst_score
            worst_year = curr_worst_year

        curr_best_year = max(win_avg_per_year, key=win_avg_per_year.get)
        curr_best_score = win_avg_per_year[curr_best_year]
        if curr_best_score > best_avg_yearly:
            best_team_yearly = curr_team
            best_avg_yearly = curr_best_score
            best_year = curr_best_year

    highlighted_teams = {
        "best average in one year: %s, %s - %.2f" % (best_team_yearly, best_year, best_avg_yearly): best_team_yearly,
        "worst average in one year: %s, %s - %.2f" % (
            worst_team_yearly, worst_year, worst_avg_yearly): worst_team_yearly,
    }

    fig, ax = plt.subplots(figsize=(10, 5))
    for curr_team, curr_stats in home_games_win_avg_per_year_per_team.items():
        plt_with_disruption(ax, list(curr_stats.keys()), list(curr_stats.values()),
                            c=cm.gray(0.8), alpha=0.2, label='_nolegend_')

    colors = iter(['red', 'green', 'purple', 'blue'])
    for curr_descr, curr_team in highlighted_teams.items():
        curr_team_stats = home_games_win_avg_per_year_per_team[curr_team]
        plt_with_disruption(ax, curr_team_stats.keys(), curr_team_stats.values(),
                            c=next(colors), label=curr_descr)

    plt.xlabel('decade')
    plt.ylabel('win average per team')
    plt.title('Win Average Per Team')
    plt.ylim((0.2, 0.9))
    plt.legend()

    return '- test description 1'
