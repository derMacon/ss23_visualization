import numpy as np

MIN_TEAM_LIFETIME_YEARS = 10


def get_available_teams(df):
    return np.unique(df[['v_name_translate', 'h_name_translate']].values.ravel())


def get_available_years(df):
    return np.unique(df[['date_year']].values.ravel())


def extract_game_count(df):
    games_per_year_overall = df.groupby('date_year').size().to_dict()
    games_total_overall = df.shape[0]

    games_per_year_per_team = {}
    games_total_per_team = {}

    teams = get_available_teams(df)
    years = get_available_years(df)
    for curr_team in teams:
        curr_team_games = \
            df[(df['v_name_translate'] == curr_team)
               | (df['h_name_translate'] == curr_team)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        games_per_year_per_team[curr_team] = {element: 0 for element in years}
        games_per_year_per_team[curr_team].update(curr_team_games)
        games_total_per_team[curr_team] = sum(curr_team_games.values())

    return {
        'games_per_year_per_team': games_per_year_per_team,
        'games_total_per_team': games_total_per_team,
        'games_per_year_overall': games_per_year_overall,
        'games_total_overall': games_total_overall,
    }


def extract_win_stats(df):
    home_games_won_per_year = {}
    home_games_won_total = {}

    visiting_games_won_per_year = {}
    visiting_games_won_total = {}

    overall_games_won_per_year = {}
    overall_games_won_total = {}

    teams = get_available_teams(df)
    years = get_available_years(df)

    for curr_team in teams:
        curr_home_games_won = \
            df[(df['h_name_translate'] == curr_team)
               & (df['h_score'] > df['v_score'])
               & (df['date_h_duration'] > MIN_TEAM_LIFETIME_YEARS)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_visiting_games_won = \
            df[(df['v_name_translate'] == curr_team)
               & (df['h_score'] < df['v_score'])
               & (df['date_v_duration'] > MIN_TEAM_LIFETIME_YEARS)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_merged_wins = {key: curr_home_games_won.get(key, 0) + curr_visiting_games_won.get(key, 0)
                            for key in set(curr_home_games_won) | set(curr_visiting_games_won)}

        home_games_won_per_year[curr_team] = {element: 0 for element in years}
        visiting_games_won_per_year[curr_team] = {element: 0 for element in years}
        overall_games_won_per_year[curr_team] = {element: 0 for element in years}

        if len(curr_home_games_won) > 0:
            home_games_won_per_year[curr_team].update(dict(sorted(curr_home_games_won.items())))

        if len(curr_visiting_games_won) > 0:
            visiting_games_won_per_year[curr_team].update(dict(sorted(curr_visiting_games_won.items())))

        if len(curr_merged_wins) > 0:
            overall_games_won_per_year[curr_team].update(dict(sorted(curr_merged_wins.items())))

        home_games_won_total[curr_team] = sum(curr_home_games_won.values())
        visiting_games_won_total[curr_team] = sum(curr_visiting_games_won.values())
        overall_games_won_total[curr_team] = sum(curr_merged_wins.values())

    return {
        'home_games_won_per_year': home_games_won_per_year,
        'home_games_won_total': home_games_won_total,
        'visiting_games_won_per_year': visiting_games_won_per_year,
        'visiting_games_won_total': visiting_games_won_total,
        'overall_games_won_per_year': overall_games_won_per_year,
        'overall_games_won_total': overall_games_won_total
    }

    def calc_win_averages(df):
        win_stats = extract_win_stats(df)
        game_count_stats = extract_game_count(df)

        win_avg_per_year_per_team = {}
        win_avg_total_per_team = {}

        # TODO implement this

        return {
            'win_avg_per_year_per_team': win_avg_per_year_per_team,
            'win_avg_total_per_team': win_avg_total_per_team,
        }


    # average_wins_per_year[curr_team] = sum(curr_merged_wins.values()) / len(curr_merged_wins)
    # win_ratio_per_year[curr_team] = average_wins_per_year[curr_team] / games_per_year

    # TODO check if this function is actually needed somewhere - else delete
    def calc_years_without_data(df):
        available_years = df['date_year'].unique()
        start = min(available_years)
        end = max(available_years)

        total_years = np.arange(start, end + 1)
        out = list(set(total_years) - set(available_years))
        print('unavailable years: ', out)

        return out
