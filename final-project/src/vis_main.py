from src.utils.graph_data_io import read_game_logs, export_graph
from src.plots.score import score_plot

df = read_game_logs()

# export_graph(score_plot.v_score_count, df)
# export_graph(score_plot.h_score_count, df)
# export_graph(score_plot.vh_score_comparison, df)
export_graph(score_plot.winning_teams, df)

# export_graph(event_plot.data_per_year, df)
# export_graph(event_plot.data_per_decade, df)
# export_graph(event_plot.attendance_per_year, df)
# export_graph(event_plot.attendance_per_decade, df)
