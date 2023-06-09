import numpy as np
from datetime import datetime
import pandas as pd



# df = pd.read_csv('../datasets/test/test.csv', sep=',', header=None)

def convert_to_datetime64(date_string):
    datetime_obj = datetime.strptime(date_string, '%Y%m%d')
    return np.datetime64(datetime_obj, 'D')


dtypeDict = {
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
    'h_line_score': np.int32,
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
    'v_intentional': np.int32,
    'walks': np.int32,
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
    'h_intentional': np.int32,
    'walks': np.int32,
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

# # dtypeDict['completion'] = str
# # dtypeDict['forefeit'] = str
# dtypeDict['protest'] = str
# dtypeDict['park_id'] = str
# dtypeDict['attendance'] = str
# dtypeDict['length_minutes'] = str
# dtypeDict['v_line_score'] = str
# dtypeDict['h_line_score'] = str
# dtypeDict['v_at_bats'] = str
# dtypeDict['v_hits'] = str
# dtypeDict['v_doubles'] = str
# dtypeDict['v_triples'] = str
# dtypeDict['v_homeruns'] = str
# dtypeDict['v_rbi'] = str
# dtypeDict['v_sacrifice_hits'] = str
# dtypeDict['v_sacrifice_flies'] = str
# dtypeDict['v_hit_by_pitch'] = str
# dtypeDict['v_walks'] = str
# dtypeDict['v_intentional'] = str
# dtypeDict['walks'] = str
# dtypeDict['v_strikeouts'] = str
# dtypeDict['v_stolen_bases'] = str
# dtypeDict['v_caught_stealing'] = str
# dtypeDict['v_grounded_into_double'] = str
# dtypeDict['v_first_catcher_interference'] = str
# dtypeDict['v_left_on_base'] = str
# dtypeDict['v_pitchers_used'] = str
# dtypeDict['v_individual_earned_runs'] = str
# dtypeDict['v_team_earned_runs'] = str
# dtypeDict['v_wild_pitches'] = str
# dtypeDict['v_balks'] = str
# dtypeDict['v_putouts'] = str
# dtypeDict['v_assists'] = str
# dtypeDict['v_errors'] = str
# dtypeDict['v_passed_balls'] = str
# dtypeDict['v_double_plays'] = str
# dtypeDict['v_triple_plays'] = str
# dtypeDict['h_at_bats'] = str
# dtypeDict['h_hits'] = str
# dtypeDict['h_doubles'] = str
# dtypeDict['h_triples'] = str
# dtypeDict['h_homeruns'] = str
# dtypeDict['h_rbi'] = str
# dtypeDict['h_sacrifice_hits'] = str
# dtypeDict['h_sacrifice_flies'] = str
# dtypeDict['h_hit_by_pitch'] = str
# dtypeDict['h_walks'] = str
# dtypeDict['h_intentional'] = str
# dtypeDict['walks'] = str
# dtypeDict['h_strikeouts'] = str
# dtypeDict['h_stolen_bases'] = str
# dtypeDict['h_caught_stealing'] = str
# dtypeDict['h_grounded_into_double'] = str
# dtypeDict['h_first_catcher_interference'] = str
# dtypeDict['h_left_on_base'] = str
# dtypeDict['h_pitchers_used'] = str
# dtypeDict['h_individual_earned_runs'] = str
# dtypeDict['h_team_earned_runs'] = str
# dtypeDict['h_wild_pitches'] = str
# dtypeDict['h_balks'] = str
# dtypeDict['h_putouts'] = str
# dtypeDict['h_assists'] = str
# dtypeDict['h_errors'] = str
# dtypeDict['h_passed_balls'] = str
# dtypeDict['h_double_plays'] = str
# dtypeDict['h_triple_plays'] = str
# dtypeDict['hp_umpire_id'] = str
# dtypeDict['hp_umpire_name'] = str
# dtypeDict['1b_umpire_id'] = str
# dtypeDict['1b_umpire_name'] = str
# dtypeDict['2b_umpire_id'] = str
# dtypeDict['2b_umpire_name'] = str
# dtypeDict['3b_umpire_id'] = str
# dtypeDict['3b_umpire_name'] = str
# dtypeDict['lf_umpire_id'] = str
# dtypeDict['lf_umpire_name'] = str
# dtypeDict['rf_umpire_id'] = str
# dtypeDict['rf_umpire_name'] = str
# dtypeDict['v_manager_id'] = str
# dtypeDict['v_manager_name'] = str
# dtypeDict['h_manager_id'] = str
# dtypeDict['h_manager_name'] = str
# dtypeDict['winning_pitcher_id'] = str
# dtypeDict['winning_pitcher_name'] = str
# dtypeDict['losing_pitcher_id'] = str
# dtypeDict['losing_pitcher_name'] = str
# dtypeDict['saving_pitcher_id'] = str
# dtypeDict['saving_pitcher_name'] = str
# dtypeDict['winning_rbi_batter_id'] = str
# dtypeDict['winning_rbi_batter_id_name'] = str
# dtypeDict['v_starting_pitcher_id'] = str
# dtypeDict['v_starting_pitcher_name'] = str
# dtypeDict['h_starting_pitcher_id'] = str
# dtypeDict['h_starting_pitcher_name'] = str
# dtypeDict['v_player_1_id'] = str
# dtypeDict['v_player_1_name'] = str
# dtypeDict['v_player_1_def_pos'] = str
# dtypeDict['v_player_2_id'] = str
# dtypeDict['v_player_2_name'] = str
# dtypeDict['v_player_2_def_pos'] = str
# dtypeDict['v_player_3_id'] = str
# dtypeDict['v_player_3_name'] = str
# dtypeDict['v_player_3_def_pos'] = str
# dtypeDict['v_player_4_id'] = str
# dtypeDict['v_player_4_name'] = str
# dtypeDict['v_player_4_def_pos'] = str
# dtypeDict['v_player_5_id'] = str
# dtypeDict['v_player_5_name'] = str
# dtypeDict['v_player_5_def_pos'] = str
# dtypeDict['v_player_6_id'] = str
# dtypeDict['v_player_6_name'] = str
# dtypeDict['v_player_6_def_pos'] = str
# dtypeDict['v_player_7_id'] = str
# dtypeDict['v_player_7_name'] = str
# dtypeDict['v_player_7_def_pos'] = str
# dtypeDict['v_player_8_id'] = str
# dtypeDict['v_player_8_name'] = str
# dtypeDict['v_player_8_def_pos'] = str
# dtypeDict['v_player_9_id'] = str
# dtypeDict['v_player_9_name'] = str
# dtypeDict['v_player_9_def_pos'] = str
# dtypeDict['h_player_1_id'] = str
# dtypeDict['h_player_1_name'] = str
# dtypeDict['h_player_1_def_pos'] = str
# dtypeDict['h_player_2_id'] = str
# dtypeDict['h_player_2_name'] = str
# dtypeDict['h_player_2_def_pos'] = str
# dtypeDict['h_player_3_id'] = str
# dtypeDict['h_player_3_name'] = str
# dtypeDict['h_player_3_def_pos'] = str
# dtypeDict['h_player_4_id'] = str
# dtypeDict['h_player_4_name'] = str
# dtypeDict['h_player_4_def_pos'] = str
# dtypeDict['h_player_5_id'] = str
# dtypeDict['h_player_5_name'] = str
# dtypeDict['h_player_5_def_pos'] = str
# dtypeDict['h_player_6_id'] = str
# dtypeDict['h_player_6_name'] = str
# dtypeDict['h_player_6_def_pos'] = str
# dtypeDict['h_player_7_id'] = str
# dtypeDict['h_player_7_name'] = str
# dtypeDict['h_player_7_def_pos'] = str
# dtypeDict['h_player_8_id'] = str
# dtypeDict['h_player_8_name'] = str
# dtypeDict['h_player_8_def_pos'] = str
# dtypeDict['h_player_9_id'] = str
# dtypeDict['h_player_9_name'] = str
# dtypeDict['h_player_9_def_pos'] = str
# dtypeDict['additional_info'] = str
# dtypeDict['acquisition_info'] = str

df = pd.read_csv('../datasets/retrosheets/game-logs_combined/game_logs_data-world_minimal.csv', sep=',', dtype=dtypeDict)

df['date'] = df['date'].apply(convert_to_datetime64)

print(df.values)

# data = np.genfromtxt('../datasets/retrosheets/game-logs_combined/game_logs_data-world.csv')
# print("data: ", data)
