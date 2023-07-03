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
    data_per_year = df.groupby(['date_year']).size().to_dict()
    lifetime_data = calc_team_lifetimes(df)

    fig, ax_plot = plt.subplots(figsize=(10, 5))
    plt_with_disruption(ax_plot, data_per_year.keys(), data_per_year.values(), label='data rows per year')
    log.debug("team_lifetimes: %s", lifetime_data['team_lifetimes'])

    ax_bar = ax_plot.twinx()
    team_lifetimes = lifetime_data['team_lifetimes']
    sorted_teams_by_first_year = lifetime_data['sorted_teams_by_first_year']

    for curr_team, curr_first_year in sorted_teams_by_first_year.items():
        ax_bar.barh(curr_team, width=team_lifetimes[curr_team], left=curr_first_year, color='gray', alpha=0.5)

    selected_teams = ['Boston - Braves']
    ax_bar.set_yticks(range(len(sorted_teams_by_first_year)))
    ax_bar.set_yticklabels([team if team in selected_teams else '' for team in sorted_teams_by_first_year.keys()])

    ax_plot.set_xlabel('decade')
    ax_plot.set_ylabel('gmaes per year')
    ax_bar.set_ylabel('team lifetimes')
    plt.title('Active teams per year vs. games played')
    plt.legend()

    plt.subplots_adjust(right=0.8)
