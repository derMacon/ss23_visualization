import matplotlib.pyplot as plt
import numpy as np

def courts_v_score(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    quota = []

    for current_courts in courts:
        #home_games_won = df.loc[(df['park_id'] == current_courts), 'h_score'].sum()
        home_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] > df['v_score'])] \
            .groupby('park_id') \
            .size() \
            .to_dict()
        home_games_won = home_games_won.get(current_courts)

        #visiting_games_won = df.loc[(df['park_id'] == current_courts), 'v_score'].sum()
        visiting_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] < df['v_score'])] \
            .groupby('park_id') \
            .size() \
            .to_dict()
        visiting_games_won = visiting_games_won.get(current_courts)

        # if current_courts in home_games_won and int(home_games_won.get(current_courts)) >= 10 and int(visiting_games_won.get(current_courts)) >= 10:
        if home_games_won!=None and home_games_won >= 10 and visiting_games_won >= 10:
            res = home_games_won / visiting_games_won
            quota.append(res)
            names.append(current_courts)

            if res >= 2.0:
                print(current_courts)
                print(f"quota :  {res}")
                print(home_games_won + visiting_games_won)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, quota)

def courts_homeruns(df):
    courts = np.unique(df[['park_id']].values.ravel())

    names = []
    amount = []

    for current_courts in courts:
        home_homeruns = df.loc[(df['park_id'] == current_courts), 'v_homeruns'].sum()
        visiting_homeruns = df.loc[(df['park_id'] == current_courts), 'h_homeruns'].sum()



        print(home_homeruns)

        if(home_homeruns > 5):
            names.append(current_courts)
            amount.append(home_homeruns + visiting_homeruns)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, amount)

def courts_homeruns_comp(df):
    courts = np.unique(df[['park_id']].values.ravel())

    names = []
    amount_h = []
    amount_v = []

    for current_courts in courts:
        home_homeruns = df.loc[(df['park_id'] == current_courts), 'v_homeruns'].sum()
        visiting_homeruns = df.loc[(df['park_id'] == current_courts), 'h_homeruns'].sum()


        if(home_homeruns > 10):
            names.append(current_courts)
            amount_h.append(home_homeruns )
            amount_v.append(visiting_homeruns)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, amount_h)
    plt.scatter(names, amount_v)

def courts_homeruns_comp2(df):
    courts = np.unique(df[['park_id']].values.ravel())

    names = []
    ratio = []

    for current_courts in courts:
        home_homeruns = df.loc[(df['park_id'] == current_courts), 'v_homeruns'].sum()
        visiting_homeruns = df.loc[(df['park_id'] == current_courts), 'h_homeruns'].sum()


        if(home_homeruns > 10):
            names.append(current_courts)
            ratio.append(home_homeruns / visiting_homeruns)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, ratio)

def courts_visitors(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    amount = []
    sum = []

    for current_courts in courts:
        attendance = df.loc[(df['park_id'] == current_courts), 'attendance'].mean()
        attendance_max = df.loc[(df['park_id'] == current_courts), 'attendance'].sum()

        if attendance > 5000 and attendance is not None:
            names.append(current_courts)
            print(attendance)
            amount.append(attendance)
            sum.append(attendance_max)

        # merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, amount)
    #plt.scatter(names, sum)

def courts_visitors_max(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    amount = []
    sum = []

    for current_courts in courts:
        attendance_max = df.loc[(df['park_id'] == current_courts), 'attendance'].sum()

        if attendance_max > 1000000 and attendance_max is not None:

            names.append(current_courts)
            sum.append(attendance_max)

        # merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, sum)
