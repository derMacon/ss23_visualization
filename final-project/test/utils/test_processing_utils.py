import unittest

import pandas as pd

from src.utils.processing_utils import extract_game_count
from src.utils.processing_utils import extract_win_stats
from src.utils.processing_utils import calc_win_averages
from src.utils.logging_config import log


class ModuleTestCase(unittest.TestCase):

    def test_valid_extract_game_count(self):
        test_input = {
            'date_year': [1884, 1884, 1885, 1886],
            'v_name_translate': ['team-a', 'team-b', 'team-c', 'team-d'],
            'h_name_translate': ['team-c', 'team-c', 'team-b', 'team-e'],
        }

        game_count_stats = extract_game_count(pd.DataFrame(test_input))

        # TODO maybe leave out years, where team did not play?
        exp_games_per_year_per_team = {
            'team-a': {1884: 1, 1885: 0, 1886: 0},
            'team-b': {1884: 1, 1885: 1, 1886: 0},
            'team-c': {1884: 2, 1885: 1, 1886: 0},
            'team-d': {1884: 0, 1885: 0, 1886: 1},
            'team-e': {1884: 0, 1885: 0, 1886: 1},
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

        self.assertEqual(game_count_stats['games_per_year_per_team'], exp_games_per_year_per_team)
        self.assertEqual(game_count_stats['games_total_per_team'], exp_games_total_per_team)
        self.assertEqual(game_count_stats['games_per_year_overall'], exp_games_per_year_overall)
        self.assertEqual(game_count_stats['games_total_overall'], exp_games_total_overall)

    def test_valid_extract_win_stats(self):
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

        exp_home_games_won_per_year = {
            'team-a': {1884: 0, 1885: 0},
            'team-b': {1884: 0, 1885: 1},
            'team-c': {1884: 0, 1885: 0},
        }

        exp_home_games_won_total = {
            'team-a': 0,
            'team-b': 1,
            'team-c': 0,
        }

        exp_visiting_games_won_per_year = {
            'team-a': {1884: 1, 1885: 0},
            'team-b': {1884: 2, 1885: 0},
            'team-c': {1884: 0, 1885: 0},
        }

        exp_visiting_games_won_total = {
            'team-a': 1,
            'team-b': 2,
            'team-c': 0,
        }

        exp_overall_games_won_per_year = {
            'team-a': {1884: 1, 1885: 0},
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

    def test_valid_calc_win_averages(self):
        test_input = {
            'date_year': [1884, 1884, 1884, 1885],
            'v_name_translate': ['team-a', 'team-b', 'team-b', 'team-c'],
            'h_name_translate': ['team-c', 'team-c', 'team-a', 'team-b'],
            'v_score': [3, 1, 9, 2],
            'h_score': [2, 0, 4, 5],
            'date_v_duration': [30, 30, 30, 30],
            'date_h_duration': [30, 30, 30, 30],
        }

        win_averages = calc_win_averages(pd.DataFrame(test_input))
        log.debug('win_avg_per_year_per_team: %s', win_averages['win_avg_per_year_per_team'])
        log.debug('win_avg_total_per_team: %s', win_averages['win_avg_total_per_team'])

        exp_win_avg_per_year_per_team = {
            'team-a': {1884: 0.5},
            'team-b': {1884: 1, 1885: 1},
            'team-c': {1884: 0, 1885: 0},
        }

        exp_win_avg_total_per_team = {
            'team-a': 0.5,
            'team-b': 1,
            'team-c': 0,
        }

        self.assertEqual(win_averages['win_avg_per_year_per_team'], exp_win_avg_per_year_per_team)
        self.assertEqual(win_averages['win_avg_total_per_team'], exp_win_avg_total_per_team)


if __name__ == '__main__':
    unittest.main()
