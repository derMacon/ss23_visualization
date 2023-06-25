def merge_dicts_divide(fst_dict, snd_dict):
    assert len(fst_dict) == len(snd_dict) \
           and set(fst_dict.keys()) == set(snd_dict.keys()) \
           and 0 not in snd_dict.values()

    out = {}

    for fst_key, fst_val in fst_dict.items():
        out[fst_key] = fst_val / snd_dict[fst_key]

    return out
