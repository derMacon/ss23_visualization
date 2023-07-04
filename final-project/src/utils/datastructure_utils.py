import copy
from src.utils.logging_config import log


def merge_dicts_divide(fst_dict, snd_dict):
    assert len(fst_dict) == len(snd_dict) and set(fst_dict.keys()) == set(snd_dict.keys())

    out = {}

    for fst_key, fst_val in fst_dict.items():
        denominator = snd_dict[fst_key]

        if denominator != 0:
            out[fst_key] = fst_val / snd_dict[fst_key]
        else:
            assert denominator == 0 and fst_val == 0
            out[fst_key] = 0

    return out


def merge_dicts_add(fst_dict, snd_dict):
    out = copy.deepcopy(fst_dict)

    for snd_key, snd_val in snd_dict.items():
        if out.get(snd_key) is not None:
            out[snd_key] += snd_val
        else:
            out[snd_key] = snd_val

    return out


def merge_dicts_nested_add(fst_dict, snd_dict):
    out = copy.deepcopy(fst_dict)

    for snd_key, snd_val in snd_dict.items():
        if out.get(snd_key) is not None:
            out[snd_key] = merge_dicts_add(out[snd_key], snd_val)
        else:
            out[snd_key] = snd_val

    return out

def merge_dicts_append(fst_dict, snd_dict):
    out = copy.deepcopy(fst_dict)

    for snd_key, snd_val in snd_dict.items():
        if out.get(snd_key) is not None:
            # out[snd_key] = merge_dicts_add(out[snd_key], snd_val)
            out[snd_key].append(snd_val)
        else:
            out[snd_key] = [snd_val]

    return out


def compare_dicts_with_delta(dict1, dict2, delta):
    # Check if the dictionaries have the same keys
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Compare the values with the specified delta
    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]
        if abs(value1 - value2) > delta:
            log.debug("dicts unequal at values: %s - %s", value1, value2)
            return False

    return True

def compare_nested_dicts_with_delta(dict1, dict2, delta):
    # Check if the dictionaries have the same keys
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Compare the values with the specified delta
    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]
        if not compare_dicts_with_delta(value1, value2, delta):
            return False

    return True


def min_nested_dict(dict_input):
    tmp = {}
    for dict_key, dict_value in dict_input.items():
        min_key = min(dict_value, key=dict_value.get)
        min_value = min(dict_value, key=dict_value.get)
        tmp[dict_key] = {min_key, min_value}
    return min(tmp, key=tmp.get)