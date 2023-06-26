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
