import numpy as np

MIN_TEAM_LIFETIME_YEARS = 10


def extract_games_per_year(df):
    return df.groupby('date_year').size().to_dict()


def extract_win_stats(input_df):
    home_games_won_per_year = {}
    visiting_games_won_per_year = {}
    overall_games_won_per_year = {}
    overall_games_won_total_sorted = {}
    average_wins_per_year = {}
    win_ratio_per_year = {}

    games_per_year = extract_games_per_year(input_df)
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
            win_ratio_per_year[curr_team] = average_wins_per_year[curr_team] / games_per_year

    return home_games_won_per_year, \
        visiting_games_won_per_year, \
        overall_games_won_per_year, \
        overall_games_won_total_sorted, \
        average_wins_per_year, \
        win_ratio_per_year


# TODO check if this function is actually needed somewhere - else delete
def calc_years_without_data(df):
    available_years = df['date_year'].unique()
    start = min(available_years)
    end = max(available_years)

    total_years = np.arange(start, end + 1)
    out = list(set(total_years) - set(available_years))
    print('unavailable years: ', out)

    return out
