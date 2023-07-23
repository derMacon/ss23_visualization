from plots.courts import courts_plot
import utils.graph_data_io
import event_plot
from plots.score import score_plot
from plots.courts import courts_plot
from plots.weeks import week_plot
from utils.graph_data_io import *

exporter = GraphExporter()

exporter.append_section('Main Plots')

#exporter.append_subsection('Leo Graphs - TODO rename')

exporter.append_graph(courts_plot.courts_v_score)
exporter.append_graph(courts_plot.courts_total_score_vs_attendance)
exporter.append_graph(courts_plot.courts_homeruns)
exporter.append_graph(courts_plot.courts_visitors_together)

exporter.append_graph(week_plot.weekday_importance)

exporter.append_subsection('Score Comparison')
exporter.append_graph(score_plot.v_score_count)
exporter.append_graph(score_plot.h_score_count)
exporter.append_graph(score_plot.vh_score_comparison_plt)
exporter.append_graph(score_plot.vh_score_comparison_bar)
exporter.append_graph(score_plot.winning_teams)

exporter.append_subsection('Meta Data')
exporter.append_graph(event_plot.games_per_year_per_team)
exporter.append_graph(event_plot.attendance_per_year)
exporter.append_graph(event_plot.data_per_year)
exporter.append_graph(teams_plot.active_teams_per_year)
exporter.append_graph(teams_plot.comparing_games_played_with_active_teams_per_year)

exporter.append_subsection('Winning Averages')
exporter.append_graph(score_plot.win_ratio_teams)
exporter.append_graph(score_plot.home_win_avg)

#exporter.append_subsection('Winning Averages')
#exporter.append_graph(score_plot.win_ratio_teams)
#exporter.append_graph(score_plot.home_win_avg)

exporter.append_section('Additional Plots')
exporter.append_subsection('Incomplete Drafts')
# TODO - filter out graphs

exporter.build_presentation()
