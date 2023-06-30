import unittest

import pandas as pd

from src.utils.processing_utils import *
from src.utils.datastructure_utils import *
from src.utils.logging_config import log


class ModuleTestCase(unittest.TestCase):

    def test_get_available_teams1(self):
        test_input = {
            'v_name_translate': ['team-a'],
            'h_name_translate': ['team-b'],
            'date_h_duration': [30],
            'date_v_duration': [30],
        }

        act_teams = set(get_available_teams(pd.DataFrame(test_input)))
        exp_teams = set(['team-a', 'team-b'])

        log.debug('act_teams: %s', act_teams)
        log.debug('exp_teams: %s', exp_teams)
        self.assertEqual(act_teams, exp_teams)

    def test_get_available_teams2(self):
        test_input = {
            'h_name_translate': ['team-a'],
            'v_name_translate': ['team-b'],
            'date_h_duration': [30],
            'date_v_duration': [0],
        }

        act_teams = set(get_available_teams(pd.DataFrame(test_input), 30))
        exp_teams = set(['team-a'])

        log.debug('act_teams: %s', act_teams)
        log.debug('exp_teams: %s', exp_teams)
        self.assertEqual(exp_teams, act_teams)

    def test_valid_extract_game_count(self):
        test_input = {
            'date_year': [1884, 1884, 1885, 1886],
            'v_name_translate': ['team-a', 'team-b', 'team-c', 'team-d'],
            'h_name_translate': ['team-c', 'team-c', 'team-b', 'team-e'],
        }

        game_count_stats = extract_game_count(pd.DataFrame(test_input))

        exp_games_per_year_per_team = {
            'team-a': {1884: 1},
            'team-b': {1884: 1, 1885: 1},
            'team-c': {1884: 2, 1885: 1},
            'team-d': {1886: 1},
            'team-e': {1886: 1},
        }

        exp_games_total_per_team = {
            'team-a': 1,
            'team-b': 2,
            'team-c': 3,
            'team-d': 1,
            'team-e': 1,
        }

        exp_games_per_year_overall = {
            1884: 2,
            1885: 1,
            1886: 1,
        }

        exp_games_total_overall = 4

        exp_home_games_per_year_per_team = {
            'team-a': {},
            'team-b': {1885: 1},
            'team-c': {1884: 2},
            'team-d': {},
            'team-e': {1886: 1},
        }

        exp_visiting_games_per_year_per_team = {
            'team-a': {1884: 1},
            'team-b': {1884: 1},
            'team-c': {1885: 1},
            'team-d': {1886: 1},
            'team-e': {},
        }

        log.debug('games_per_year_per_team: %s', game_count_stats['games_per_year_per_team'])
        log.debug('exp_games_per_year_per_team: %s', exp_games_per_year_per_team)
        self.assertEqual(game_count_stats['games_per_year_per_team'], exp_games_per_year_per_team)

        log.debug('games_total_per_team: %s', game_count_stats['games_total_per_team'])
        log.debug('exp_games_total_per_team: %s', exp_games_total_per_team)
        self.assertEqual(game_count_stats['games_total_per_team'], exp_games_total_per_team)

        log.debug('games_per_year_overall: %s', game_count_stats['games_per_year_overall'])
        log.debug('exp_games_per_year_overall: %s', exp_games_per_year_overall)
        self.assertEqual(game_count_stats['games_per_year_overall'], exp_games_per_year_overall)

        log.debug('games_total_overall: %s', game_count_stats['games_total_overall'])
        log.debug('exp_games_total_overall: %s', exp_games_total_overall)
        self.assertEqual(game_count_stats['games_total_overall'], exp_games_total_overall)

        log.debug('home_games_per_year_per_team: %s', game_count_stats['home_games_per_year_per_team'])
        log.debug('exp_home_games_per_year_per_team: %s', exp_home_games_per_year_per_team)
        self.assertEqual(game_count_stats['home_games_per_year_per_team'], exp_home_games_per_year_per_team)

        log.debug('visiting_games_per_year_per_team: %s', game_count_stats['visiting_games_per_year_per_team'])
        log.debug('exp_visiting_games_per_year_per_team: %s', exp_visiting_games_per_year_per_team)
        self.assertEqual(game_count_stats['visiting_games_per_year_per_team'], exp_visiting_games_per_year_per_team)

    def test_valid_extract_win_stats1(self):
        test_input = {
            'date_year': [1884, 1884, 1884, 1885],
            'v_name_translate': ['team-a', 'team-b', 'team-b', 'team-c'],
            'h_name_translate': ['team-c', 'team-c', 'team-a', 'team-b'],
            'v_score': [3, 1, 9, 2],
            'h_score': [2, 0, 4, 5],
            'date_v_duration': [30, 30, 30, 30],
            'date_h_duration': [30, 30, 30, 30],
        }

        game_count_stats = extract_win_stats(pd.DataFrame(test_input))

        log.debug('home_games_won_per_year: %s', game_count_stats['home_games_won_per_year'])
        log.debug('home_games_won_total: %s', game_count_stats['home_games_won_total'])
        log.debug('visiting_games_won_per_year: %s', game_count_stats['visiting_games_won_per_year'])
        log.debug('visiting_games_won_total: %s', game_count_stats['visiting_games_won_total'])
        log.debug('overall_games_won_per_year: %s', game_count_stats['overall_games_won_per_year'])
        log.debug('overall_games_won_total: %s', game_count_stats['overall_games_won_total'])

        exp_home_games_won_per_year = {
            'team-a': {1884: 0},
            'team-b': {1885: 1},
            'team-c': {1884: 0},
        }

        exp_home_games_won_total = {
            'team-a': 0,
            'team-b': 1,
            'team-c': 0,
        }

        exp_visiting_games_won_per_year = {
            'team-a': {1884: 1},
            'team-b': {1884: 2},
            'team-c': {1885: 0},
        }

        exp_visiting_games_won_total = {
            'team-a': 1,
            'team-b': 2,
            'team-c': 0,
        }

        exp_overall_games_won_per_year = {
            'team-a': {1884: 1},
            'team-b': {1884: 2, 1885: 1},
            'team-c': {1884: 0, 1885: 0},
        }

        exp_overall_games_won_total = {
            'team-a': 1,
            'team-b': 3,
            'team-c': 0,
        }

        self.assertEqual(game_count_stats['home_games_won_per_year'], exp_home_games_won_per_year)
        self.assertEqual(game_count_stats['home_games_won_total'], exp_home_games_won_total)
        self.assertEqual(game_count_stats['visiting_games_won_per_year'], exp_visiting_games_won_per_year)
        self.assertEqual(game_count_stats['visiting_games_won_total'], exp_visiting_games_won_total)
        self.assertEqual(game_count_stats['overall_games_won_per_year'], exp_overall_games_won_per_year)
        self.assertEqual(game_count_stats['overall_games_won_total'], exp_overall_games_won_total)

    def test_valid_extract_win_stats2(self):
        test_input = {
            'date_year': [1884],
            'v_name_translate': ['team-a'],
            'h_name_translate': ['team-b'],
            'v_score': [3],
            'h_score': [2],
            'date_v_duration': [30],
            'date_h_duration': [30],
        }

        game_count_stats = extract_win_stats(pd.DataFrame(test_input))

        exp_home_games_won_per_year = {
            'team-b': {1884: 0},
        }

        exp_home_games_won_total = {
            'team-b': 0,
        }

        exp_visiting_games_won_per_year = {
            'team-a': {1884: 1},
        }

        exp_visiting_games_won_total = {
            'team-a': 1,
        }

        exp_overall_games_won_per_year = {
            'team-a': {1884: 1},
            'team-b': {1884: 0},
        }

        exp_overall_games_won_total = {
            'team-a': 1,
            'team-b': 0,
        }

        log.debug('home_games_won_per_year: %s', game_count_stats['home_games_won_per_year'])
        log.debug('exp_home_games_won_per_year: %s', exp_home_games_won_per_year)
        self.assertEqual(game_count_stats['home_games_won_per_year'], exp_home_games_won_per_year)

        log.debug('home_games_won_total: %s', game_count_stats['home_games_won_total'])
        log.debug('exp_home_games_won_total: %s', exp_home_games_won_total)
        self.assertEqual(game_count_stats['home_games_won_total'], exp_home_games_won_total)

        log.debug('visiting_games_won_per_year: %s', game_count_stats['visiting_games_won_per_year'])
        log.debug('exp_visiting_games_won_per_year: %s', exp_visiting_games_won_per_year)
        self.assertEqual(game_count_stats['visiting_games_won_per_year'], exp_visiting_games_won_per_year)

        log.debug('visiting_games_won_total: %s', game_count_stats['visiting_games_won_total'])
        log.debug('exp_visiting_games_won_total: %s', exp_visiting_games_won_total)
        self.assertEqual(game_count_stats['visiting_games_won_total'], exp_visiting_games_won_total)

        log.debug('overall_games_won_per_year: %s', game_count_stats['overall_games_won_per_year'])
        log.debug('exp_overall_games_won_per_year: %s', exp_overall_games_won_per_year)
        self.assertEqual(game_count_stats['overall_games_won_per_year'], exp_overall_games_won_per_year)

        log.debug('overall_games_won_total: %s', game_count_stats['overall_games_won_total'])
        log.debug('exp_overall_games_won_total: %s', exp_overall_games_won_total)
        self.assertEqual(game_count_stats['overall_games_won_total'], exp_overall_games_won_total)

    def test_valid_calc_win_averages1(self):
        test_input = {
            'date_year': [1884, 1884, 1884, 1885, 1886, 1886, 1887],
            'v_name_translate': ['team-a', 'team-b', 'team-b', 'team-c', 'team-d', 'team-d', 'team-e'],
            'h_name_translate': ['team-c', 'team-c', 'team-a', 'team-b', 'team-e', 'team-f', 'team-d'],
            'v_score': [3, 1, 9, 2, 0, 1, 0],
            'h_score': [2, 0, 4, 5, 1, 0, 1],
            'date_v_duration': [30, 30, 30, 30, 30, 30, 30],
            'date_h_duration': [30, 30, 30, 30, 30, 30, 30],
        }

        win_averages = calc_win_averages(pd.DataFrame(test_input))

        exp_win_avg_per_year_per_team = {
            'team-a': {1884: 0.5},
            'team-b': {1884: 1.0, 1885: 1.0},
            'team-c': {1884: 0.0, 1885: 0.0},
            'team-d': {1886: 0.5, 1887: 1.0},
            'team-e': {1886: 1.0, 1887: 0.0},
            'team-f': {1886: 0.0},
        }

        exp_win_avg_total_per_team = {
            'team-a': 0.5,
            'team-b': 1.0,
            'team-c': 0.0,
            'team-d': 0.66,
            'team-e': 0.5,
            'team-f': 0.0,
        }

        exp_home_games_win_avg_per_year_per_team = {
            'team-a': {1884: 0.0},
            'team-b': {1885: 1.0},
            'team-c': {1884: 0.0},
            'team-d': {1887: 1.0},
            'team-e': {1886: 1.0},
            'team-f': {1886: 0.0},
        }

        exp_visiting_games_win_avg_per_year_per_team = {
            'team-a': {1884: 1.0},
            'team-b': {1884: 1.0},
            'team-c': {1885: 0.0},
            'team-d': {1886: 0.5},
            'team-e': {1887: 0.0},
        }

        log.debug('win_avg_per_year_per_team: %s', win_averages['win_avg_per_year_per_team'])
        log.debug('exp_win_avg_per_year_per_team: %s', exp_win_avg_per_year_per_team)
        self.assertEqual(win_averages['win_avg_per_year_per_team'], exp_win_avg_per_year_per_team)

        log.debug('win_avg_total_per_team: %s', win_averages['win_avg_total_per_team'])
        log.debug('exp_win_avg_total_per_team: %s', exp_win_avg_total_per_team)
        self.assertTrue(
            compare_dicts_with_delta(win_averages['win_avg_total_per_team'], exp_win_avg_total_per_team, 0.01))

        log.debug('home_games_win_avg_per_year_per_team: %s', win_averages['home_games_win_avg_per_year_per_team'])
        log.debug('exp_home_games_win_avg_per_year_per_team: %s', exp_home_games_win_avg_per_year_per_team)
        self.assertEqual(win_averages['home_games_win_avg_per_year_per_team'], exp_home_games_win_avg_per_year_per_team)

        log.debug('visiting_games_win_avg_per_year_per_team: %s',
                  win_averages['visiting_games_win_avg_per_year_per_team'])
        log.debug('exp_visiting_games_win_avg_per_year_per_team: %s', exp_visiting_games_win_avg_per_year_per_team)
        self.assertEqual(win_averages['visiting_games_win_avg_per_year_per_team'],
                         exp_visiting_games_win_avg_per_year_per_team)

    def test_valid_calc_win_averages2(self):
        test_input = {
            'date_year': [1884, 1884, 1884, 1885, 1885, 1885, 1885],
            'v_name_translate': ['team-a', 'team-a', 'team-b', 'team-a', 'team-a', 'team-a', 'team-b'],
            'h_name_translate': ['team-b', 'team-b', 'team-a', 'team-b', 'team-b', 'team-b', 'team-a'],
            'v_score': [1, 1, 1, 1, 1, 1, 1],
            'h_score': [0, 0, 0, 0, 0, 0, 0],
            'date_v_duration': [30, 30, 30, 30, 30, 30, 30],
            'date_h_duration': [30, 30, 30, 30, 30, 30, 30],
        }

        win_averages = calc_win_averages(pd.DataFrame(test_input))

        exp_win_avg_per_year_per_team = {
            'team-a': {1884: 0.66, 1885: 0.75},
            'team-b': {1884: 0.33, 1885: 0.25},
        }

        exp_win_avg_total_per_team = {
            'team-a': 0.705,
            'team-b': 0.29,
        }

        exp_home_games_win_avg_per_year_per_team = {
            'team-a': {1884: 0, 1885: 0},
            'team-b': {1884: 0, 1885: 0},
        }

        exp_visiting_games_win_avg_per_year_per_team = {
            'team-a': {1884: 1.0, 1885: 1.0},
            'team-b': {1884: 1.0, 1885: 1.0},
        }

        log.debug('win_avg_per_year_per_team: %s', win_averages['win_avg_per_year_per_team'])
        log.debug('exp_win_avg_per_year_per_team: %s', exp_win_avg_per_year_per_team)
        self.assertTrue(
            compare_nested_dicts_with_delta(win_averages['win_avg_per_year_per_team'], exp_win_avg_per_year_per_team,
                                            0.01))

        log.debug('win_avg_total_per_team: %s', win_averages['win_avg_total_per_team'])
        log.debug('exp_win_avg_total_per_team: %s', exp_win_avg_total_per_team)
        self.assertTrue(
            compare_dicts_with_delta(win_averages['win_avg_total_per_team'], exp_win_avg_total_per_team, 0.01))

        log.debug('home_games_win_avg_per_year_per_team: %s', win_averages['home_games_win_avg_per_year_per_team'])
        log.debug('exp_home_games_win_avg_per_year_per_team: %s', exp_home_games_win_avg_per_year_per_team)
        self.assertEqual(win_averages['home_games_win_avg_per_year_per_team'], exp_home_games_win_avg_per_year_per_team)

        log.debug('visiting_games_win_avg_per_year_per_team: %s',
                  win_averages['visiting_games_win_avg_per_year_per_team'])
        log.debug('exp_visiting_games_win_avg_per_year_per_team: %s', exp_visiting_games_win_avg_per_year_per_team)
        self.assertEqual(win_averages['visiting_games_win_avg_per_year_per_team'],
                         exp_visiting_games_win_avg_per_year_per_team)


if __name__ == '__main__':
    unittest.main()
