import copy


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


