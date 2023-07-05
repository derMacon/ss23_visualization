from src.plots.meta import event_plot
from src.plots.meta import teams_plot
from src.plots.score import score_plot
from src.utils.graph_data_io import *

df = read_game_logs()

# export_graph(score_plot.v_score_count, df)
# export_graph(score_plot.h_score_count, df)
# export_graph(score_plot.vh_score_comparison, df)
# export_graph(score_plot.winning_teams, df)
#
# export_graph(event_plot.data_per_year, df)
# export_graph(event_plot.attendance_per_year, df)
# export_graph(event_plot.games_per_year_per_team, df)
#
# export_graph(teams_plot.active_teams_per_year, df)
# export_graph(teams_plot.comparing_games_played_with_active_teams_per_year, df)
#
# export_graph(score_plot.win_ratio_teams, df)

export_graph(score_plot.home_win_avg, df)
