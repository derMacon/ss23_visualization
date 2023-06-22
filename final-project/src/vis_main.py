from src.utils.graph_data_io import read_game_logs, export_graph
from src.plots.score import graph_plot

df = read_game_logs()

export_graph(graph_plot.plot_v_score_count, df)
export_graph(graph_plot.plot_h_score_count, df)
export_graph(graph_plot.plot_vh_score_comparison, df)
