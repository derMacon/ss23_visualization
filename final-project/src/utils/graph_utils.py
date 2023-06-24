import matplotlib.pyplot as plt

# TODO create custom color pallet etc.


def merge_add_dict(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
