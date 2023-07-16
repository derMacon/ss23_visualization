import matplotlib.pyplot as plt
import numpy as np

def courts_v_score(df):
    courts = np.unique(df[['park_id']].values.ravel())

    wins_per_year = {}

    for current_courts in courts:
        home_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] > df['v_score'])] \
            .groupby('date_decade') \
            .size() \
            .to_dict()

        visiting_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] < df['v_score'])] \
            .groupby('date_decade') \
            .size() \
            .to_dict()

        merged_wins = {key: home_games_won.get(key, 0) + visiting_games_won.get(key, 0)
                       for key in set(home_games_won) | set(visiting_games_won)}

        wins_per_year[current_courts] = merged_wins