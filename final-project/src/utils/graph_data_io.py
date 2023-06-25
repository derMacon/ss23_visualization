import numpy as np
import inspect
import os
import matplotlib.pyplot as plt
import pandas as pd

from src.utils.logging_config import log

GAME_LOGS_DATA_WORLD = '../datasets/retrosheets/game-logs_combined/game_logs_data-world.csv'
GAME_LOGS_ABBREVIATIONS = '../datasets/retrosheets/game-logs_combined/TEAMABR.TXT'
OUTPUT_DIR = '../graphs'

_dtypeDict = {
    'date': str,
    'number_of_game': np.uint32,
    'day_of_week': str,
    'v_name': str,
    'v_league': str,
    'v_game_number': np.int32,
    'h_name': str,
    'h_league': str,
    'h_game_number': np.int32,
    'v_score': np.int32,
    'h_score': np.int32,
    'length_outs': np.int32,
    'day_night': str,
    'completion': str,
    'forefeit': str,
    'protest': str,
    'park_id': str,
    'attendance': np.int32,
    'length_minutes': np.int32,
    'v_line_score': str,
    'h_line_score': str,
    'v_at_bats': np.int32,
    'v_hits': np.int32,
    'v_doubles': np.int32,
    'v_triples': np.int32,
    'v_homeruns': np.int32,
    'v_rbi': np.int32,
    'v_sacrifice_hits': np.int32,
    'v_sacrifice_flies': np.int32,
    'v_hit_by_pitch': np.int32,
    'v_walks': np.int32,
    'v_intentional walks': np.int32,
    'v_strikeouts': np.int32,
    'v_stolen_bases': np.int32,
    'v_caught_stealing': np.int32,
    'v_grounded_into_double': np.int32,
    'v_first_catcher_interference': np.int32,
    'v_left_on_base': np.int32,
    'v_pitchers_used': np.int32,
    'v_individual_earned_runs': np.int32,
    'v_team_earned_runs': np.int32,
    'v_wild_pitches': np.int32,
    'v_balks': np.int32,
    'v_putouts': np.int32,
    'v_assists': np.int32,
    'v_errors': np.int32,
    'v_passed_balls': np.int32,
    'v_double_plays': np.int32,
    'v_triple_plays': np.int32,
    'h_at_bats': np.int32,
    'h_hits': np.int32,
    'h_doubles': np.int32,
    'h_triples': np.int32,
    'h_homeruns': np.int32,
    'h_rbi': np.int32,
    'h_sacrifice_hits': np.int32,
    'h_sacrifice_flies': np.int32,
    'h_hit_by_pitch': np.int32,
    'h_walks': np.int32,
    'h_intentional walks': np.int32,
    'h_strikeouts': np.int32,
    'h_stolen_bases': np.int32,
    'h_caught_stealing': np.int32,
    'h_grounded_into_double': np.int32,
    'h_first_catcher_interference': np.int32,
    'h_left_on_base': np.int32,
    'h_pitchers_used': np.int32,
    'h_individual_earned_runs': np.int32,
    'h_team_earned_runs': np.int32,
    'h_wild_pitches': np.int32,
    'h_balks': np.int32,
    'h_putouts': np.int32,
    'h_assists': np.int32,
    'h_errors': np.int32,
    'h_passed_balls': np.int32,
    'h_double_plays': np.int32,
    'h_triple_plays': np.int32,
    'hp_umpire_id': str,
    'hp_umpire_name': str,
    '1b_umpire_id': str,
    '1b_umpire_name': str,
    '2b_umpire_id': str,
    '2b_umpire_name': str,
    '3b_umpire_id': str,
    '3b_umpire_name': str,
    'lf_umpire_id': str,
    'lf_umpire_name': str,
    'rf_umpire_id': str,
    'rf_umpire_name': str,
    'v_manager_id': str,
    'v_manager_name': str,
    'h_manager_id': str,
    'h_manager_name': str,
    'winning_pitcher_id': str,
    'winning_pitcher_name': str,
    'losing_pitcher_id': str,
    'losing_pitcher_name': str,
    'saving_pitcher_id': str,
    'saving_pitcher_name': str,
    'winning_rbi_batter_id': str,
    'winning_rbi_batter_id_name': str,
    'v_starting_pitcher_id': str,
    'v_starting_pitcher_name': str,
    'h_starting_pitcher_id': str,
    'h_starting_pitcher_name': str,
    'v_player_1_id': str,
    'v_player_1_name': str,
    'v_player_1_def_pos': np.int32,
    'v_player_2_id': str,
    'v_player_2_name': str,
    'v_player_2_def_pos': np.int32,
    'v_player_3_id': str,
    'v_player_3_name': str,
    'v_player_3_def_pos': np.int32,
    'v_player_4_id': str,
    'v_player_4_name': str,
    'v_player_4_def_pos': np.int32,
    'v_player_5_id': str,
    'v_player_5_name': str,
    'v_player_5_def_pos': np.int32,
    'v_player_6_id': str,
    'v_player_6_name': str,
    'v_player_6_def_pos': np.int32,
    'v_player_7_id': str,
    'v_player_7_name': str,
    'v_player_7_def_pos': np.int32,
    'v_player_8_id': str,
    'v_player_8_name': str,
    'v_player_8_def_pos': np.int32,
    'v_player_9_id': str,
    'v_player_9_name': str,
    'v_player_9_def_pos': np.int32,
    'h_player_1_id': str,
    'h_player_1_name': str,
    'h_player_1_def_pos': np.int32,
    'h_player_2_id': str,
    'h_player_2_name': str,
    'h_player_2_def_pos': np.int32,
    'h_player_3_id': str,
    'h_player_3_name': str,
    'h_player_3_def_pos': np.int32,
    'h_player_4_id': str,
    'h_player_4_name': str,
    'h_player_4_def_pos': np.int32,
    'h_player_5_id': str,
    'h_player_5_name': str,
    'h_player_5_def_pos': np.int32,
    'h_player_6_id': str,
    'h_player_6_name': str,
    'h_player_6_def_pos': np.int32,
    'h_player_7_id': str,
    'h_player_7_name': str,
    'h_player_7_def_pos': np.int32,
    'h_player_8_id': str,
    'h_player_8_name': str,
    'h_player_8_def_pos': np.int32,
    'h_player_9_id': str,
    'h_player_9_name': str,
    'h_player_9_def_pos': np.int32,
    'additional_info': str,
    'acquisition_info': str
}


def _process_value(value):
    if value == '':
        return
    else:
        return value


def _empty_flags_for_empty_cells(gamelog_df):
    # deal with null / empty values
    placeholder = '-12345'
    # fill empty cells with placeholder
    gamelog_df = gamelog_df.fillna(placeholder)
    # necessary to cast with type dictionary
    gamelog_df = gamelog_df.astype(_dtypeDict)
    # after cast insert nan value, for an early fail in later processing if list
    # is not properly sanitized
    gamelog_df = gamelog_df.replace(int(placeholder), np.nan)
    gamelog_df = gamelog_df.replace(placeholder, None)
    return gamelog_df


def _sanitize_df(gamelog_df):
    gamelog_df = _empty_flags_for_empty_cells(gamelog_df)
    return gamelog_df


def _append_date_summaries(gamelog_df):
    """
    appends new values to input dataframe
    - date_year: year in which the game took place
    - date_decade: decade in wich the game took place
    :param gamelog_df: input dataframe
    :return: appended dataframe
    """
    # create a new column containing just the year - easier for later processing
    gamelog_df['date'] = pd.to_datetime(gamelog_df['date'])
    gamelog_df = pd.concat([gamelog_df, gamelog_df['date'].apply(lambda x: x.year).rename('date_year')], axis=1)
    gamelog_df = pd.concat(
        [gamelog_df, gamelog_df['date'].apply(lambda x: str(x.year)[:3] + '0s').rename('date_decade')], axis=1)
    return gamelog_df


def _append_team_ids_translation(gamelog_df):
    """
    appends new values to input dataframe
    - v_name_translate: city and full name of the visiting team combined
    - h_name_translate: city and full name of the home team combined
    :param gamelog_df: input dataframe
    :return: appended dataframe
    """
    # translate team ids
    abreviations_df = pd.read_csv(GAME_LOGS_ABBREVIATIONS)
    team_mapping = dict(zip(abreviations_df['team'], abreviations_df['city'] + ' - ' + abreviations_df['nickname']))
    gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(team_mapping).rename('v_name_translate')], axis=1)
    gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(team_mapping).rename('h_name_translate')], axis=1)

    return gamelog_df


def _append_team_duration(gamelog_df):
    """
    appends new values to input dataframe
    - date_h_duration: years which the home team existed
    - date_v_duration: years which the visiting team existed
    :param gamelog_df: input dataframe
    :return: appended dataframe
    """
    abreviations_df = pd.read_csv(GAME_LOGS_ABBREVIATIONS)
    duration_mapping = dict(zip(abreviations_df['team'], abreviations_df['last_year'] - abreviations_df['first_year']))
    gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(duration_mapping).rename('date_h_duration')], axis=1)
    gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(duration_mapping).rename('date_v_duration')], axis=1)

    return gamelog_df


def _add_custom_fields(gamelog_df):
    gamelog_df = _append_date_summaries(gamelog_df)
    gamelog_df = _append_team_ids_translation(gamelog_df)
    gamelog_df = _append_team_duration(gamelog_df)
    return gamelog_df


def read_game_logs():
    log.info('started reading csv dataset')

    debug_row_count = os.environ.get('VIS_ROW_COUNT')

    if debug_row_count is not None:
        log.info("debug flag set, only reading %s entries", debug_row_count)
        df = pd.read_csv(GAME_LOGS_DATA_WORLD, converters={col: _process_value for col in _dtypeDict.keys()},
                         nrows=int(debug_row_count))
    else:
        df = pd.read_csv(GAME_LOGS_DATA_WORLD, converters={col: _process_value for col in _dtypeDict.keys()})
    log.info('finished reading csv dataset')

    df = _sanitize_df(df)
    df = _add_custom_fields(df)

    return df


def export_graph(plotting_func, df):
    callback_package_name = inspect.getmodule(plotting_func).__package__.replace(".", "/")
    callback_file_name = os.path.splitext(os.path.basename(inspect.getfile(plotting_func)))[0]
    callback_func_name = plotting_func.__name__

    output_dir = OUTPUT_DIR + '/' + callback_package_name + '/' + callback_file_name + '/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plotting_func(df)

    output_file = os.path.realpath(output_dir + callback_func_name)
    log.info('writing plot: %s', output_file)

    plt.savefig(output_file)
    plt.show()
