import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from src.utils.processing_utils import *
from src.utils.styling_utils import *
from src.utils.logging_config import log


def team_lifetimes(df):
    lifetime_data = calc_team_lifetimes(df)
    log.debug("team_lifetimes: %s", lifetime_data['team_lifetimes'])

    # df = df[df['attendance'].notna()]
    #
    # means_v_score = df.groupby(['date_year'])['attendance'].mean().to_dict()
    # x_vals = list(means_v_score.keys())
    # plt_with_disruption(plt, x_vals, means_v_score.values(), c='red', label='mean')
    #
    # plt.title('attendance')
    # plt.legend()
    #
