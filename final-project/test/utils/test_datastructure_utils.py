import unittest
from src.utils.datastructure_utils import *
from src.utils.logging_config import log


class ModuleTestCase(unittest.TestCase):

    def test_valid1_merge_dicts_divide(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 6}
        snd_input = {'1882': 4, '1884': 12, '1889': 12}
        exp_output = {'1884': 1, '1882': 9, '1889': 0.5}

        result = merge_dicts_divide(fst_input, snd_input)
        self.assertEqual(result, exp_output)

    def test_valid2_merge_dicts_divide(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 0}
        snd_input = {'1882': 4, '1884': 12, '1889': 0}
        exp_output = {'1884': 1, '1882': 9, '1889': 0}

        result = merge_dicts_divide(fst_input, snd_input)
        self.assertEqual(result, exp_output)

    def test_invalid1_merge_dicts_divide(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 6}
        snd_input = {'1884': 4, '1882': 12, '1881': 12, '1889': 12}

        with self.assertRaises(AssertionError):
            merge_dicts_divide(fst_input, snd_input)

    def test_invalid2_merge_dicts_divide(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 6}
        snd_input = {'1884': 0, '1882': 12, '1889': 12}

        merge_dicts_divide(snd_input, fst_input)
        with self.assertRaises(AssertionError):
            merge_dicts_divide(fst_input, snd_input)

    def test_valid_merge_dicts_add(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 6}
        snd_input = {'1884': 2, '1890': 12}
        exp_output = {'1884': 14, '1882': 36, '1889': 6, '1890': 12}
        log.debug('exp_output: %s', exp_output)

        fst_result = merge_dicts_add(fst_input, snd_input)
        log.debug('fst_result: %s', fst_result)
        self.assertEqual(fst_result, exp_output)

        snd_result = merge_dicts_add(fst_input, snd_input)
        log.debug('snd_result: %s', snd_result)
        self.assertEqual(fst_result, exp_output)

    def test_valid_merge_dicts_nested_add(self):
        fst_input = {
            'team-a': {},
            'team-b': {'1884': 12, '1882': 36, '1889': 6},
        }

        snd_input = {
            'team-a': {'1884': 4},
            'team-b': {'1884': 3},
        }

        exp_output = {
            'team-a': {'1884': 4},
            'team-b': {'1884': 15, '1882': 36, '1889': 6},
        }

        log.debug('exp_output: %s', exp_output)

        fst_result = merge_dicts_nested_add(fst_input, snd_input)
        log.debug('fst_result: %s', fst_result)
        self.assertEqual(fst_result, exp_output)

        snd_result = merge_dicts_nested_add(fst_input, snd_input)
        log.debug('snd_result: %s', snd_result)
        self.assertEqual(fst_result, exp_output)


if __name__ == '__main__':
    unittest.main()
