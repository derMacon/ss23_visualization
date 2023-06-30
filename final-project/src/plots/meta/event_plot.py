import matplotlib.pyplot as plt
import numpy as np

from src.utils.processing_utils import extract_game_count
from src.utils.logging_config import log


def attendance_per_year(df):
    df = df[df['attendance'].notna()]

    means_v_score = df.groupby(['date_year'])['attendance'].mean().to_dict()
    means_v_score = {str(key): value for key, value in means_v_score.items()}

    x_vals = list(means_v_score.keys())
    plt.plot(x_vals, means_v_score.values(), color='red', label='mean')

    # plt.xticks(x_vals[::5]) # only display every nth value on the x axis
    decades = sorted(df['date_decade'].unique())[1::2]
    plt.xticks(np.linspace(0, len(x_vals) - 1, len(decades)), decades)  # Spread labels evenly

    plt.title('attendance')
    plt.legend()


def data_per_year(df):
    data_per_year = df.groupby(['date_year']).size()
    plt.plot(data_per_year)


def games_per_year_overall(df):
    data = extract_game_count(df)['games_per_year_overall']
    log.debug('games_per_year: %s', data)
    plt.plot(list(data.keys()), list(data.values()))
