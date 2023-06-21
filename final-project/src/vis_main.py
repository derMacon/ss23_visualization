from game_log_importer import read_game_logs as game_logs
import graph_plot

df = game_logs()
graph_plot.plot_v_score_count(df)
