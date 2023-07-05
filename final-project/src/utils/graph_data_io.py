import numpy as np
import shutil
import inspect
import os
import matplotlib.pyplot as plt
import pandas as pd
import pypandoc
import subprocess
import time

from src.utils.logging_config import log


class GraphExporter:
    GAME_LOGS_DATA_WORLD = '../datasets/retrosheets/game-logs_combined/game_logs_data-world.csv'
    GAME_LOGS_ABBREVIATIONS = '../datasets/retrosheets/game-logs_combined/TEAMABR.TXT'
    TEX_TEMPLATE_SLIDE = '../slides/graphs/tex/_template/slide.template'
    TEX_TEMPLATE_CHAPTER = '../slides/graphs/tex/_template/section.template'
    TEX_TEMPLATE_MAIN = '../slides/graphs/tex/_template/main.template'

    OUTPUT_DIR = '../slides/graphs/img'
    OUTPUT_PDF = '../slides/pdf'
    OUTPUT_BEAMER = '../slides/graphs/tex/src/generated'

    START_YEAR = 1900

    def __init__(self):
        self.plots = []
        self._dtypeDict = {
            'date': str,
            'number_of_game': np.uint32,
            'day_of_week': str,
            'v_name': str,
            'v_league': str,
            'v_game_number': np.int32,
            'h_name': str,
            'h_league': str,
            'h_game_number': np.int32,
            'v_score': np.int32,
            'h_score': np.int32,
            'length_outs': np.int32,
            'day_night': str,
            'completion': str,
            'forefeit': str,
            'protest': str,
            'park_id': str,
            'attendance': np.int32,
            'length_minutes': np.int32,
            'v_line_score': str,
            'h_line_score': str,
            'v_at_bats': np.int32,
            'v_hits': np.int32,
            'v_doubles': np.int32,
            'v_triples': np.int32,
            'v_homeruns': np.int32,
            'v_rbi': np.int32,
            'v_sacrifice_hits': np.int32,
            'v_sacrifice_flies': np.int32,
            'v_hit_by_pitch': np.int32,
            'v_walks': np.int32,
            'v_intentional walks': np.int32,
            'v_strikeouts': np.int32,
            'v_stolen_bases': np.int32,
            'v_caught_stealing': np.int32,
            'v_grounded_into_double': np.int32,
            'v_first_catcher_interference': np.int32,
            'v_left_on_base': np.int32,
            'v_pitchers_used': np.int32,
            'v_individual_earned_runs': np.int32,
            'v_team_earned_runs': np.int32,
            'v_wild_pitches': np.int32,
            'v_balks': np.int32,
            'v_putouts': np.int32,
            'v_assists': np.int32,
            'v_errors': np.int32,
            'v_passed_balls': np.int32,
            'v_double_plays': np.int32,
            'v_triple_plays': np.int32,
            'h_at_bats': np.int32,
            'h_hits': np.int32,
            'h_doubles': np.int32,
            'h_triples': np.int32,
            'h_homeruns': np.int32,
            'h_rbi': np.int32,
            'h_sacrifice_hits': np.int32,
            'h_sacrifice_flies': np.int32,
            'h_hit_by_pitch': np.int32,
            'h_walks': np.int32,
            'h_intentional walks': np.int32,
            'h_strikeouts': np.int32,
            'h_stolen_bases': np.int32,
            'h_caught_stealing': np.int32,
            'h_grounded_into_double': np.int32,
            'h_first_catcher_interference': np.int32,
            'h_left_on_base': np.int32,
            'h_pitchers_used': np.int32,
            'h_individual_earned_runs': np.int32,
            'h_team_earned_runs': np.int32,
            'h_wild_pitches': np.int32,
            'h_balks': np.int32,
            'h_putouts': np.int32,
            'h_assists': np.int32,
            'h_errors': np.int32,
            'h_passed_balls': np.int32,
            'h_double_plays': np.int32,
            'h_triple_plays': np.int32,
            'hp_umpire_id': str,
            'hp_umpire_name': str,
            '1b_umpire_id': str,
            '1b_umpire_name': str,
            '2b_umpire_id': str,
            '2b_umpire_name': str,
            '3b_umpire_id': str,
            '3b_umpire_name': str,
            'lf_umpire_id': str,
            'lf_umpire_name': str,
            'rf_umpire_id': str,
            'rf_umpire_name': str,
            'v_manager_id': str,
            'v_manager_name': str,
            'h_manager_id': str,
            'h_manager_name': str,
            'winning_pitcher_id': str,
            'winning_pitcher_name': str,
            'losing_pitcher_id': str,
            'losing_pitcher_name': str,
            'saving_pitcher_id': str,
            'saving_pitcher_name': str,
            'winning_rbi_batter_id': str,
            'winning_rbi_batter_id_name': str,
            'v_starting_pitcher_id': str,
            'v_starting_pitcher_name': str,
            'h_starting_pitcher_id': str,
            'h_starting_pitcher_name': str,
            'v_player_1_id': str,
            'v_player_1_name': str,
            'v_player_1_def_pos': np.int32,
            'v_player_2_id': str,
            'v_player_2_name': str,
            'v_player_2_def_pos': np.int32,
            'v_player_3_id': str,
            'v_player_3_name': str,
            'v_player_3_def_pos': np.int32,
            'v_player_4_id': str,
            'v_player_4_name': str,
            'v_player_4_def_pos': np.int32,
            'v_player_5_id': str,
            'v_player_5_name': str,
            'v_player_5_def_pos': np.int32,
            'v_player_6_id': str,
            'v_player_6_name': str,
            'v_player_6_def_pos': np.int32,
            'v_player_7_id': str,
            'v_player_7_name': str,
            'v_player_7_def_pos': np.int32,
            'v_player_8_id': str,
            'v_player_8_name': str,
            'v_player_8_def_pos': np.int32,
            'v_player_9_id': str,
            'v_player_9_name': str,
            'v_player_9_def_pos': np.int32,
            'h_player_1_id': str,
            'h_player_1_name': str,
            'h_player_1_def_pos': np.int32,
            'h_player_2_id': str,
            'h_player_2_name': str,
            'h_player_2_def_pos': np.int32,
            'h_player_3_id': str,
            'h_player_3_name': str,
            'h_player_3_def_pos': np.int32,
            'h_player_4_id': str,
            'h_player_4_name': str,
            'h_player_4_def_pos': np.int32,
            'h_player_5_id': str,
            'h_player_5_name': str,
            'h_player_5_def_pos': np.int32,
            'h_player_6_id': str,
            'h_player_6_name': str,
            'h_player_6_def_pos': np.int32,
            'h_player_7_id': str,
            'h_player_7_name': str,
            'h_player_7_def_pos': np.int32,
            'h_player_8_id': str,
            'h_player_8_name': str,
            'h_player_8_def_pos': np.int32,
            'h_player_9_id': str,
            'h_player_9_name': str,
            'h_player_9_def_pos': np.int32,
            'additional_info': str,
            'acquisition_info': str
        }
        self._df = self._read_game_logs()

    def _read_game_logs(self):
        log.info('started reading csv dataset')

        debug_row_count = os.environ.get('VIS_ROW_COUNT')
        log.debug("reading data from %s entries", self.GAME_LOGS_DATA_WORLD)

        if debug_row_count is not None:
            log.info("debug flag set, only reading %s entries", debug_row_count)
            df = pd.read_csv(self.GAME_LOGS_DATA_WORLD,
                             converters={col: self._process_value for col in self._dtypeDict.keys()},
                             nrows=int(debug_row_count))
        else:
            df = pd.read_csv(self.GAME_LOGS_DATA_WORLD,
                             converters={col: self._process_value for col in self._dtypeDict.keys()})
        log.info('finished reading csv dataset')

        df = self._sanitize_df(df)
        df = self._add_custom_fields(df)

        return df

    def _process_value(self, value):
        if value == '':
            return
        else:
            return value

    def _sanitize_df(self, gamelog_df):
        gamelog_df = self._empty_flags_for_empty_cells(gamelog_df)
        gamelog_df = self._remove_first_incomplete_years(gamelog_df)
        return gamelog_df

    def _empty_flags_for_empty_cells(self, gamelog_df):
        # deal with null / empty values
        placeholder = '-12345'
        # fill empty cells with placeholder
        gamelog_df = gamelog_df.fillna(placeholder)
        # necessary to cast with type dictionary
        gamelog_df = gamelog_df.astype(self._dtypeDict)
        # after cast insert nan value, for an early fail in later processing if list
        # is not properly sanitized
        gamelog_df = gamelog_df.replace(int(placeholder), np.nan)
        gamelog_df = gamelog_df.replace(placeholder, None)
        return gamelog_df

    def _remove_first_incomplete_years(self, gameslog_df):
        # return gameslog_df[int(gameslog_df['date']) >= 18900000]
        return gameslog_df[gameslog_df['date'].apply(lambda x: int(x[:4])) >= self.START_YEAR]
        # return gameslog_df[gameslog_df['date_year'] >= 1890]

    def _add_custom_fields(self, gamelog_df):
        gamelog_df = self._append_date_summaries(gamelog_df)
        gamelog_df = self._append_team_ids_translation(gamelog_df)
        gamelog_df = self._append_team_duration(gamelog_df)
        return gamelog_df

    def _append_date_summaries(self, gamelog_df):
        """
        appends new values to input dataframe
        - date_year: year in which the game took place
        - date_decade: decade in wich the game took place
        :param gamelog_df: input dataframe
        :return: appended dataframe
        """
        # create a new column containing just the year - easier for later processing
        gamelog_df['date'] = pd.to_datetime(gamelog_df['date'])
        gamelog_df = pd.concat([gamelog_df, gamelog_df['date'].apply(lambda x: x.year).rename('date_year')], axis=1)
        gamelog_df = pd.concat(
            [gamelog_df, gamelog_df['date'].apply(lambda x: str(x.year)[:3] + '0s').rename('date_decade')], axis=1)
        return gamelog_df

    def _append_team_ids_translation(self, gamelog_df):
        """
        appends new values to input dataframe
        - v_name_translate: city and full name of the visiting team combined
        - h_name_translate: city and full name of the home team combined
        :param gamelog_df: input dataframe
        :return: appended dataframe
        """
        # translate team ids
        abreviations_df = pd.read_csv(self.GAME_LOGS_ABBREVIATIONS)
        team_mapping = dict(zip(abreviations_df['team'], abreviations_df['city'] + ' - ' + abreviations_df['nickname']))
        gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(team_mapping).rename('v_name_translate')], axis=1)
        gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(team_mapping).rename('h_name_translate')], axis=1)

        return gamelog_df

    def _append_team_duration(self, gamelog_df):
        """
        appends new values to input dataframe
        - date_h_duration: years which the home team existed
        - date_v_duration: years which the visiting team existed
        :param gamelog_df: input dataframe
        :return: appended dataframe
        """
        abreviations_df = pd.read_csv(self.GAME_LOGS_ABBREVIATIONS)
        duration_mapping = dict(
            zip(abreviations_df['team'], abreviations_df['last_year'] - abreviations_df['first_year']))
        gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(duration_mapping).rename('date_h_duration')],
                               axis=1)
        gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(duration_mapping).rename('date_v_duration')],
                               axis=1)

        first_year_mapping = dict(zip(abreviations_df['team'], abreviations_df['first_year']))
        gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(first_year_mapping).rename('date_h_first_year')],
                               axis=1)
        gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(first_year_mapping).rename('date_v_first_year')],
                               axis=1)

        last_year_mapping = dict(zip(abreviations_df['team'], abreviations_df['last_year']))
        gamelog_df = pd.concat([gamelog_df, gamelog_df['h_name'].map(last_year_mapping).rename('date_h_last_year')],
                               axis=1)
        gamelog_df = pd.concat([gamelog_df, gamelog_df['v_name'].map(last_year_mapping).rename('date_v_last_year')],
                               axis=1)

        return gamelog_df

    def _export_graph(self, plotting_func, df):
        callback_package_name = inspect.getmodule(plotting_func).__package__.replace(".", "/")
        callback_file_name = os.path.splitext(os.path.basename(inspect.getfile(plotting_func)))[0]
        callback_func_name = plotting_func.__name__

        output_dir = self.OUTPUT_DIR + '/' + callback_package_name + '/' + callback_file_name + '/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        markdown_plot_description = plotting_func(df)

        output_file = os.path.realpath(output_dir + callback_func_name)
        log.info('writing plot: %s', output_file)

        plt.savefig(output_file)
        plt.show()

        return (output_file, markdown_plot_description)

    def append_graph(self, plotting_func):
        description_tuple = self._export_graph(plotting_func, self._df)
        self.plots.append(description_tuple)

    def _load_str_content(self, file_path):
        file_content = ''
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    def _convert_md_to_latex(self, markdown_text):
        try:
            if markdown_text is None or len(markdown_text) == 0:
                return ""

            latex_text = pypandoc.convert_text(markdown_text, 'latex', format='md')
            return latex_text.replace("\\tightlist", "")

        except RuntimeError as e:
            print("Error:", e)

    def _write_latex(self, output_dir, tex_content):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = output_dir + "/" + 'ss23_visualization_mlb.tex'
        with open(output_file, 'w') as file:
            log.info("writing tex content to: %s", output_file)
            file.write(tex_content)

        return os.path.abspath(output_file)

    def _compile_tex_file(self, tex_file):
        dir = os.path.dirname(tex_file)
        subprocess.run(["pdflatex", tex_file], cwd=dir)
        subprocess.run(["pdflatex", tex_file], cwd=dir)
        return tex_file.replace(".tex", ".pdf")

    def build_presentation(self):
        latex_slide_template = self._load_str_content(self.TEX_TEMPLATE_SLIDE)
        latex_chapter_template = self._load_str_content(self.TEX_TEMPLATE_CHAPTER)
        latex_main_template = self._load_str_content(self.TEX_TEMPLATE_MAIN)

        tex_slides = ''
        for (img_path, plt_description) in self.plots:
            markdown_description = self._convert_md_to_latex(plt_description)
            presentation_slide = latex_slide_template % (img_path, markdown_description)
            tex_slides += presentation_slide

        chapter_latex = latex_chapter_template % ('Plots', tex_slides)
        main_latex = latex_main_template % chapter_latex

        tex_file = self._write_latex(self.OUTPUT_BEAMER, main_latex)
        beamer_output = self._compile_tex_file(tex_file)
        log.debug("beamer output: %s", beamer_output)
        log.debug("copy to: %s", self.OUTPUT_PDF)
        shutil.copy(beamer_output, self.OUTPUT_PDF)


