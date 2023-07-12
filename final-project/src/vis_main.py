from src.plots.meta import event_plot
from src.plots.meta import teams_plot
from src.plots.score import score_plot
from src.utils.graph_data_io import *

exporter = GraphExporter()

exporter.append_section('Main Plots')

exporter.append_subsection('Score Comparison')
exporter.append_graph(score_plot.v_score_count)
exporter.append_graph(score_plot.h_score_count)
exporter.append_graph(score_plot.vh_score_comparison_plt)
exporter.append_graph(score_plot.vh_score_comparison_boxplot)
exporter.append_graph(score_plot.winning_teams)

exporter.append_subsection('Meta Data')
exporter.append_graph(event_plot.data_per_year)
exporter.append_graph(event_plot.attendance_per_year)
exporter.append_graph(event_plot.games_per_year_per_team)
exporter.append_graph(teams_plot.active_teams_per_year)
exporter.append_graph(teams_plot.comparing_games_played_with_active_teams_per_year)

exporter.append_subsection('Winning Averages')
exporter.append_graph(score_plot.win_ratio_teams)
exporter.append_graph(score_plot.home_win_avg)

exporter.build_presentation()
