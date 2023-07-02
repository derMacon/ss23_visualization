from src.utils.graph_data_io import read_game_logs, export_graph
from src.plots.score import score_plot
from src.plots.meta import event_plot
from src.plots.meta import teams_plot

df = read_game_logs()

# export_graph(score_plot.v_score_count, df)
# export_graph(score_plot.h_score_count, df)
# export_graph(score_plot.vh_score_comparison, df)
# export_graph(score_plot.winning_teams, df)
#
# export_graph(event_plot.data_per_year, df)
# export_graph(event_plot.attendance_per_year, df)
# export_graph(event_plot.games_per_year_overall, df)
# export_graph(event_plot.games_per_year_per_team, df)

# export_graph(event_plot.team_lifetimes, df)
teams_plot.team_lifetimes(df)
