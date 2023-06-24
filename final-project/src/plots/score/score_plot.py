import matplotlib.pyplot as plt
import numpy as np


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
    teams = np.unique(df[['v_name_translate', 'h_name_translate']].values.ravel())
    # teams = ['Washington - Nationals']
    wins_per_year = {}

    fig, ax = plt.subplots()

    for curr_team in teams:

        home_games_won = df[(df['v_name_translate'] == curr_team) & (df['h_score'] > df['v_score'])] \
            .groupby('date_decade') \
            .size() \
            .to_dict()

        visiting_games_won = df[(df['h_name_translate'] == curr_team) & (df['h_score'] < df['v_score'])] \
            .groupby('date_decade') \
            .size() \
            .to_dict()

        merged_wins = {key: home_games_won.get(key, 0) + visiting_games_won.get(key, 0)
                       for key in set(home_games_won) | set(visiting_games_won)}

        wins_per_year[curr_team] = merged_wins




        # ax.plot(merged_wins.keys(), merged_wins.values(), label=curr_team)
        #
        # ax.set_xlabel('X-axis')
        # ax.set_ylabel('Y-axis')
        # ax.set_title('compare score')
        # ax.legend()

    # for (team, year), win_count in home_games_won:
    #     wins_per_year[team] =

    #     home_games_won = df[[curr_team, df['h_score'] > df['v_score']]].groupby('date_year').size().to_dict()
    #     print(home_games_won)
    # print(home_games_won)
    # home_games_won.first()
