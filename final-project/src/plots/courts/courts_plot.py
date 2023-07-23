import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd

def courts_v_score(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    quota = []
    home_win = []
    visit_win = []
    home_win_label = []
    visit_win_label = []
    names_label =[]
    amount = []
    visiters = []
    amount_total = []

    for current_courts in courts:
        #home_games_won = df.loc[(df['park_id'] == current_courts), 'h_score'].sum()
        home_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] > df['v_score'])] \
            .groupby('park_id') \
            .size() \
            .to_dict()
        home_games_won = home_games_won.get(current_courts)
        attendance = df.loc[(df['park_id'] == current_courts),"attendance"].mean()
        # attendance = df[(df['park_id'] == current_courts)].groupby('park_id').size().get(current_courts)

        #visiting_games_won = df.loc[(df['park_id'] == current_courts), 'v_score'].sum()
        visiting_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] < df['v_score'])] \
            .groupby('park_id') \
            .size() \
            .to_dict()
        visiting_games_won = visiting_games_won.get(current_courts)

        # if current_courts in home_games_won and int(home_games_won.get(current_courts)) >= 10 and int(visiting_games_won.get(current_courts)) >= 10:
        if home_games_won!=None and home_games_won >= 10 and visiting_games_won >= 10:
            res = home_games_won / visiting_games_won
            amount.append(home_games_won + visiting_games_won)
            home_win.append(home_games_won)
            visit_win.append(visiting_games_won)
            quota.append(res)
            names.append(current_courts)
            visiters.append(attendance)
            amount_total.append(df[(df['park_id'] == current_courts)].groupby('park_id').size().get(current_courts))


            #if res >= 5.0:
                #print(current_courts)
                #print(f"quota :  {res}")
                #print(home_games_won + visiting_games_won)

            if res > 1.5 and attendance > 20000 and attendance < 35000:

                home_win_label.append(res)
                visit_win_label.append(attendance)
                #names_label.append(current_courts)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter( visiters, quota , c = amount_total , cmap = "viridis")
    #plt.plot([0,3000],[0,3000],"r--")
    #plt.plot([0, 3000], [0, 3900])
    #plt.semilogy()
    #plt.semilogx()
    plt.title("home court advantage")
    plt.ylabel("home wins / visiting wins")
    plt.xlabel("average attendance")
    #plt.annotate("winning parity line", (1450,1600))
    cbar = plt.colorbar()
    #cbar.ax.set_yticklabels(['', '20m', '40m', '60m', '80m', '100m'])
    cbar.ax.get_yaxis().labelpad = 15
    cbar.set_label("games played", rotation=270)
    names_label.append("old Yankee Stadium ")
    #plt.annotate("old Yankee Stadium ", (visit_win_label[0],visit_win_label[0] ))
    print(visit_win_label)
    for name,x,y in zip(names_label,visit_win_label,home_win_label):
        plt.annotate(name, (x,y))


def courts_total_score_vs_attendance(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    quota = []
    total_score = []
    attendance = []
    visit_win = []
    home_win_label = []
    visit_win_label = []
    names_label =[]
    amount = []
    visiters = []
    mean_label = []
    total_score_label = []

    for current_courts in courts:
        #home_games_won = df.loc[(df['park_id'] == current_courts), 'h_score'].sum()
        home_score = df.loc[(df['park_id'] == current_courts), 'h_score'].mean()
        visiting_score = df.loc[(df['park_id'] == current_courts), 'v_score'].mean()

        total_score.append(home_score + visiting_score)

        #visiting_games_won = df.loc[(df['park_id'] == current_courts), 'v_score'].sum()
        attendance.append( df.loc[(df['park_id'] == current_courts), 'attendance'].mean())
        amount.append(df[(df['park_id'] == current_courts)].groupby('park_id').size().get(current_courts))
        # if current_courts in home_games_won and int(home_games_won.get(current_courts)) >= 10 and int(visiting_games_won.get(current_courts)) >= 10:

        if home_score + visiting_score > 9.8 and df[(df['park_id'] == current_courts)].groupby('park_id').size().get(current_courts) > 1000:
            total_score_label.append(home_score + visiting_score)
            mean_label.append(df.loc[(df['park_id'] == current_courts), 'attendance'].mean())
            names_label.append(current_courts)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter( attendance,total_score,c = amount, cmap = 'viridis')
    plt.xlabel("average attendance")
    plt.ylabel("average total score")
    cbar = plt.colorbar()
    #cbar.ax.set_yticklabels(['', '20m', '40m', '60m', '80m', '100m'])
    cbar.ax.get_yaxis().labelpad = 15
    cbar.set_label("total games played in the court", rotation=270)

    #for name,x,y in zip(names_label,mean_label,total_score_label):
    #    plt.annotate(name, (x,y))

#A good one
def courts_homeruns(df):
    courts = np.unique(df[['park_id']].values.ravel())

    names = []
    amount = []
    games_played = []
    ratio = []
    visiters = []
    amount_label = []
    visiters_label = []



    for current_courts in courts:
        home_homeruns = df.loc[(df['park_id'] == current_courts), 'v_homeruns'].mean()
        visiting_homeruns = df.loc[(df['park_id'] == current_courts), 'h_homeruns'].mean()
        attendance = df.loc[(df['park_id'] == current_courts), 'attendance'].mean()
        games2 = df[(df['park_id'] == current_courts)].groupby('park_id') \
            .size() \
            .to_dict()

        games = games2.get(current_courts)
        #games > 1000 and
        if(games > 500 and games is not None):

            amount.append(home_homeruns + visiting_homeruns)
            games_played.append(games)
            visiters.append(attendance)
        if(home_homeruns + visiting_homeruns > 2.5 or attendance > 35000 or (home_homeruns + visiting_homeruns < 0.7 and games > 2000)):
            amount_label.append(home_homeruns + visiting_homeruns)
            names.append(current_courts)
            visiters_label.append(attendance)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(visiters, amount, c = games_played , cmap = "viridis" )
    plt.xlabel("average attendance")
    plt.ylabel("homeruns per game")
    cbar = plt.colorbar()
    #for name, x, y in zip(names, visiters_label, amount_label):
    #    plt.annotate(name, (x, y))

    #cbar.ax.set_yticklabels(['','5', '10', '15', '20','25','30','35'])
    plt.title("do homerunns make stadiums popular?")
    cbar.ax.get_yaxis().labelpad = 15
    cbar.set_label("games played", rotation = 270)

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

    plt.scatter(names, amount, c = sum, cmap= "Greens")
    #plt.scatter(names, sum)

def courts_visitors_max(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    amount = []
    sum = []

    for current_courts in courts:
        attendance = df.loc[(df['park_id'] == current_courts), 'attendance'].mean()
        attendance_max = df.loc[(df['park_id'] == current_courts), 'attendance'].sum()

        if attendance_max > 1000000 and attendance_max is not None:
            amount.append(attendance)
            names.append(current_courts)
            sum.append(attendance_max)

        # merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(names, sum, c = amount, cmap= "Greens")

def courts_visitors_together(df):
    courts = np.unique(df[['park_id']].values.ravel())

    quota_dict = {}
    names = []
    amount = []
    sum = []
    size =[]
    record = []
    mean_label = []
    names_label = []
    rec_label = []

    for current_courts in courts:
        attendance = df.loc[(df['park_id'] == current_courts), 'attendance'].mean()
        attendance_max = df.loc[(df['park_id'] == current_courts), 'attendance'].sum()
        attendance_size = df[(df['park_id'] == current_courts)].groupby('park_id').size()
        attendance_rec = df.loc[(df['park_id'] == current_courts), 'attendance'].max()

        if attendance_max > 1000000 and attendance_max is not None:
            amount.append(attendance)
            names.append(current_courts)
            sum.append(attendance_max)
            size.append(attendance_size)
            record.append(attendance_rec)

        if attendance_max > 100000000 or attendance > 38000 or attendance_rec > 80000:
            mean_label.append(attendance)
            rec_label.append(attendance_rec)
            names_label.append(current_courts)
            #print(attendance_rec)

        # merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter(amount, record, c = sum, cmap= "viridis")
    plt.ylabel("record attendance")
    plt.xlabel("average attendance")
    cbar = plt.colorbar()
    #plt.
    #plt.lines(x = 0.5, ymin = 10000 , ymax = 70000 , color = "black")
    plt.plot([5000, 40000], [10000, 80000] , "r--")
    plt.plot([8000, 40000], [10000, 50000] , "r--")
    plt.text(33500,80000,"50% utilization")
    plt.text( 33500, 51000, "80% utilization")

    cbar.ax.set_yticklabels(['','20m', '40m', '60m', '80m','100m'])
    cbar.ax.get_yaxis().labelpad = 15
    cbar.set_label("total livetime attendance in million visitors", rotation=270)
    plt.title(" are big stadiums the most popular?")

    #for name,x,y in zip(names_label,mean_label,rec_label):
    #    plt.annotate(name, (x,y))

def court_size_range(df):
    decades = np.unique(df[['date_decade']].values.ravel())
    courts = np.unique(df[['park_id']].values.ravel())

    assembled_average_attendance = []
    plt.title("spread of average attendance through the decades")
    for current_decade in decades:
        plt.figure()
        average_attendance = []
        for current_court in courts:
            # print(df[df['date_decade'] == '1900s', 'attendance'].groupby('park_id').mean().to_dict())
            dec = df[(df['date_decade'] == current_decade)]
            x = dec.loc[(df['park_id'] == current_court), 'attendance'].mean()
            if x is not None:
                average_attendance.append(x)
        assembled_average_attendance.append(average_attendance)
        # assembled_average_attendance.set
    ax = pd.DataFrame({decades[0]: assembled_average_attendance[0]}).plot(kind='kde')
    for i in range(1,10):
        pd.DataFrame({decades[i]: assembled_average_attendance[i]}).plot(kind='kde',ax = ax)
    #frame = pd.DataFrame({decades[0]: assembled_average_attendance[0],
    #                      decades[1]: assembled_average_attendance[1],
    #                      decades[2]: assembled_average_attendance[2],
    #                      decades[3]: assembled_average_attendance[3],
    #                      decades[4]: assembled_average_attendance[4],
    #                      decades[5]: assembled_average_attendance[5],
    #                      decades[6]: assembled_average_attendance[6],
    #                      decades[7]: assembled_average_attendance[7],
    #                      decades[8]: assembled_average_attendance[8],
    #                      decades[9]: assembled_average_attendance[9]})
    #pd.DataFrame(frame).plotmo(kind='kde')
    plt.show()

    #plt.density((assembled_average_attendance[0], bw=0.5),alpha = 0.3)
    #plt.density(assembled_average_attendance[6],alpha = 0.3)
    #plt.density(assembled_average_attendance[9],alpha = 0.3)