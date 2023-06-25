import unittest
from src.utils.datastructure_utils import merge_dicts_divide


class ModuleTestCase(unittest.TestCase):

    def test_valid_merge_dicts_divide(self):
        fst_input = {'1884': 12, '1882': 36, '1889': 6}
        snd_input = {'1882': 4, '1884': 12, '1889': 12}
        exp_output = {'1884': 1, '1882': 9, '1889': 0.5}

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


if __name__ == '__main__':
    unittest.main()
