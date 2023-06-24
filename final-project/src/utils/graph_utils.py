import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MIN_TEAM_LIFETIME_YEARS = 10


# TODO create custom color pallet etc.


def extract_win_stats(input_df):
    home_games_won_per_year = {}
    visiting_games_won_per_year = {}
    overall_games_won_per_year = {}
    overall_games_won_total_sorted = {}
    average_wins_per_year = {}

    teams = np.unique(input_df[['v_name_translate', 'h_name_translate']].values.ravel())
    for curr_team in teams:
        curr_home_games_won = \
            input_df[(input_df['v_name_translate'] == curr_team)
                     & (input_df['h_score'] > input_df['v_score'])
                     & (input_df['date_v_duration'] > MIN_TEAM_LIFETIME_YEARS)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_visiting_games_won = \
            input_df[(input_df['h_name_translate'] == curr_team)
                     & (input_df['h_score'] < input_df['v_score'])
                     & (input_df['date_h_duration'] > MIN_TEAM_LIFETIME_YEARS)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_merged_wins = {key: curr_home_games_won.get(key, 0) + curr_visiting_games_won.get(key, 0)
                            for key in set(curr_home_games_won) | set(curr_visiting_games_won)}

        if len(curr_home_games_won) > 0:
            home_games_won_per_year[curr_team] = dict(sorted(curr_home_games_won.items()))

        if len(curr_visiting_games_won) > 0:
            visiting_games_won_per_year[curr_team] = dict(sorted(curr_visiting_games_won.items()))

        if len(curr_merged_wins) > 0:
            overall_games_won_per_year[curr_team] = dict(sorted(curr_merged_wins.items()))
            overall_games_won_total_sorted[curr_team] = sum(curr_merged_wins.values())
            average_wins_per_year[curr_team] = sum(curr_merged_wins.values()) / len(curr_merged_wins)

        # overall_games_won_total_sorted = dict(sorted(overall_games_won_total_sorted.items(), key=lambda x: x[1]))

    return home_games_won_per_year,\
        visiting_games_won_per_year,\
        overall_games_won_per_year,\
        overall_games_won_total_sorted, \
        average_wins_per_year
