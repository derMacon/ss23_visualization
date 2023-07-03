import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from src.utils.processing_utils import *
from src.utils.styling_utils import *
from src.utils.logging_config import log


def active_teams_per_year(df):
    lifetime_data = calc_team_lifetimes(df)
    log.debug("team_lifetimes: %s", lifetime_data['team_lifetimes'])

    fig, ax = plt.subplots()

    active_teams_per_year = lifetime_data['active_teams_per_year']
    plt_with_disruption(ax, active_teams_per_year.keys(), active_teams_per_year.values())

    ax.set_ylabel('active teams')
    ax.set_xlabel('decade')
    plt.title('Active Teams Per Year')
    plt.legend()


def team_lifetimes(df):
    # TODO implement this: Active teams per year vs. games played

    lifetime_data = calc_team_lifetimes(df)
    log.debug("team_lifetimes: %s", lifetime_data['team_lifetimes'])

    fig, ax = plt.subplots()

    team_lifetimes = lifetime_data['team_lifetimes']
    sorted_teams_by_first_year = lifetime_data['sorted_teams_by_first_year']

    for curr_team, curr_first_year in sorted_teams_by_first_year.items():
        ax.barh(curr_team, width=team_lifetimes[curr_team], left=curr_first_year, color='blue', alpha=0.5)

    active_teams_per_year = lifetime_data['active_teams_per_year']
    plt_with_disruption(ax, active_teams_per_year.keys(), active_teams_per_year.values())

    ax.set_ylabel('active teams')
    ax.set_xlabel('decade')
    plt.title('Active teams per year vs. games played')
    plt.legend()
