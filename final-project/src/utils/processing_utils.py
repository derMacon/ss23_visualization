import numpy as np
from src.utils.datastructure_utils import *
from src.utils.logging_config import log

MIN_TEAM_LIFETIME_YEARS = 10
MIN_GAMES_PLAYED_PER_YEAR = 15


def debug_set_min_team_lifetime_years(value):
    MIN_TEAM_LIFETIME_YEARS = value


def debug_min_games_played_per_year(value):
    MIN_GAMES_PLAYED_PER_YEAR = value


def extract_game_count(df, min_lifetime=MIN_TEAM_LIFETIME_YEARS):
    """
    extracting game count stats\n
    - games_per_year_per_team\n
    - games_total_per_team\n
    - games_per_year_overall\n
    - games_total_overall\n
    - visiting_games_per_year_per_team
    - home_games_per_year_per_team
    :param df: input data frame
    :return: game count stats
    """
    games_per_year_overall = df.groupby('date_year').size().to_dict()
    games_total_overall = df.shape[0]

    games_per_year_per_team = {}
    games_total_per_team = {}

    home_games_per_year_per_team = {}
    visiting_games_per_year_per_team = {}

    h_teams = np.array(df[(df['date_h_duration'] >= min_lifetime)]['h_name_translate'])
    v_teams = np.array(df[(df['date_v_duration'] >= min_lifetime)]['v_name_translate'])
    teams = np.unique(np.concatenate((h_teams, v_teams)))

    for curr_team in teams:
        home_games_per_year_per_team[curr_team] = \
            df[(df['h_name_translate'] == curr_team)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        visiting_games_per_year_per_team[curr_team] = \
            df[(df['v_name_translate'] == curr_team)] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_team_games = merge_dicts_nested_add(home_games_per_year_per_team, visiting_games_per_year_per_team)

        games_per_year_per_team[curr_team] = curr_team_games[curr_team]
        games_total_per_team[curr_team] = sum(curr_team_games[curr_team].values())

    return {
        'games_per_year_per_team': games_per_year_per_team,
        'games_total_per_team': games_total_per_team,
        'games_per_year_overall': games_per_year_overall,
        'games_total_overall': games_total_overall,
        'visiting_games_per_year_per_team': visiting_games_per_year_per_team,
        'home_games_per_year_per_team': home_games_per_year_per_team,
    }


def get_available_teams(df, min_lifetime=MIN_TEAM_LIFETIME_YEARS, min_games_played_per_year=MIN_GAMES_PLAYED_PER_YEAR):
    game_count_stats = extract_game_count(df, min_lifetime=min_lifetime)
    games_per_year_per_team = game_count_stats['games_per_year_per_team']

    teams_playing_min_count = []
    for curr_team, games_per_year in games_per_year_per_team.items():
        min_year = min(games_per_year, key=games_per_year.get)
        min_game_count = games_per_year[min_year]

        # if min_game_count >= min_games_played_per_year:
        #     log.debug('min in if: %s - %s, %s', curr_team, min_game_count, min_games_played_per_year)
        teams_playing_min_count.append(curr_team)

    log.debug('teams_playing_min_count: %s', teams_playing_min_count)
    return teams_playing_min_count


def extract_win_stats(df):
    """
    extracting win stats\n
    - home_games_won_per_year\n
    - home_games_won_total\n
    - visiting_games_won_per_year\n
    - visiting_games_won_total\n
    - overall_games_won_per_year\n
    - overall_games_won_total\n
    :param df: input dataframe
    :return: win stats
    """
    home_games_won_per_year = {}
    home_games_won_total = {}

    visiting_games_won_per_year = {}
    visiting_games_won_total = {}

    overall_games_won_per_year = {}
    overall_games_won_total = {}

    teams = get_available_teams(df)
    game_count_stats = extract_game_count(df)

    for curr_team in teams:

        init_home_games_won = {key: 0 for key in game_count_stats['home_games_per_year_per_team'][curr_team]}
        init_visiting_games_won = {key: 0 for key in game_count_stats['visiting_games_per_year_per_team'][curr_team]}

        tmp_home_games_wins = \
            df[(df['h_name_translate'] == curr_team)
               & (df['h_score'] > df['v_score'])] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        tmp_visiting_games_wins = \
            df[(df['v_name_translate'] == curr_team)
               & (df['h_score'] < df['v_score'])] \
                .groupby('date_year') \
                .size() \
                .to_dict()

        curr_home_games_won = merge_dicts_add(init_home_games_won, tmp_home_games_wins)
        curr_visiting_games_won = merge_dicts_add(init_visiting_games_won, tmp_visiting_games_wins)

        curr_merged_wins = {key: curr_home_games_won.get(key, 0) + curr_visiting_games_won.get(key, 0)
                            for key in set(curr_home_games_won) | set(curr_visiting_games_won)}

        # home_games_won_per_year[curr_team] = {element: 0 for element in years}
        # visiting_games_won_per_year[curr_team] = {element: 0 for element in years}
        # overall_games_won_per_year[curr_team] = {element: 0 for element in years}

        if len(curr_home_games_won) > 0:
            home_games_won_per_year[curr_team] = dict(sorted(curr_home_games_won.items()))
            home_games_won_total[curr_team] = sum(curr_home_games_won.values())

        if len(curr_visiting_games_won) > 0:
            visiting_games_won_per_year[curr_team] = dict(sorted(curr_visiting_games_won.items()))
            visiting_games_won_total[curr_team] = sum(curr_visiting_games_won.values())

        if len(curr_merged_wins) > 0:
            overall_games_won_per_year[curr_team] = dict(sorted(curr_merged_wins.items()))
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
    """
    calculate win averages\n
    - win_avg_per_year_per_team\n
    - win_avg_total_per_team\n
    - visiting_games_win_avg_per_year_per_team\n
    - home_games_win_avg_per_year_per_team\n
    :param df: input data frame
    :return: win average stats
    """
    win_stats = extract_win_stats(df)
    game_count_stats = extract_game_count(df)

    win_avg_per_year_per_team = {}
    win_avg_total_per_team = {}
    visiting_games_win_avg_per_year_per_team = {}
    home_games_win_avg_per_year_per_team = {}

    log.debug('games per year: %s', game_count_stats['games_per_year_per_team'])
    log.debug('overall_games_won_per_year: %s', win_stats['overall_games_won_per_year'])
    log.debug('games_per_year_per_team: %s', game_count_stats['games_per_year_per_team'])

    for curr_team in game_count_stats['games_total_per_team'].keys():

        if curr_team in win_stats['overall_games_won_total']:
            total_won_games = win_stats['overall_games_won_total'][curr_team]
            total_played_games = game_count_stats['games_total_per_team'][curr_team]
            win_avg_total_per_team[curr_team] = total_won_games / total_played_games

        if curr_team in win_stats['overall_games_won_per_year']:
            yearly_won_games = win_stats['overall_games_won_per_year'][curr_team]
            games_per_year = game_count_stats['games_per_year_per_team'][curr_team]
            win_avg_per_year_per_team[curr_team] = merge_dicts_divide(yearly_won_games, games_per_year)

        if curr_team in win_stats['visiting_games_won_per_year']:
            visiting_won_games = win_stats['visiting_games_won_per_year'][curr_team]
            visiting_games_per_year = game_count_stats['visiting_games_per_year_per_team'][curr_team]
            visiting_games_win_avg_per_year_per_team[curr_team] = merge_dicts_divide(visiting_won_games,
                                                                                     visiting_games_per_year)
        if curr_team in win_stats['home_games_won_per_year']:
            home_won_games = win_stats['home_games_won_per_year'][curr_team]
            home_games_per_year = game_count_stats['home_games_per_year_per_team'][curr_team]
            home_games_win_avg_per_year_per_team[curr_team] = merge_dicts_divide(home_won_games, home_games_per_year)

    return {
        'win_avg_per_year_per_team': win_avg_per_year_per_team,
        'win_avg_total_per_team': win_avg_total_per_team,
        'visiting_games_win_avg_per_year_per_team': visiting_games_win_avg_per_year_per_team,
        'home_games_win_avg_per_year_per_team': home_games_win_avg_per_year_per_team,
    }

    # TODO check if this function is actually needed somewhere - else delete
    def calc_years_without_data(df):
        available_years = df['date_year'].unique()
        start = min(available_years)
        end = max(available_years)

        total_years = np.arange(start, end + 1)
        out = list(set(total_years) - set(available_years))
        print('unavailable years: ', out)

        return out
