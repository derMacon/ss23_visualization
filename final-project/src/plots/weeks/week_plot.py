import matplotlib.pyplot as plt
import numpy as np

def weekday_importance(df):
    decades = np.unique(df[['date_decade']].values.ravel())

    mo = []
    di = []
    mi_bot = []
    mi = []
    do_bot = []
    do = []
    fr_bot = []
    fr = []
    sa_bot = []
    sa = []
    so_bot = []
    so = []
    total = []
    i = 1
    count = []
    for current_decade in decades:
        dec =  df.loc[(df['date_decade'] == current_decade)]
        tot = df.loc[(df['date_decade'] == current_decade), 'attendance'].sum()
        mon = dec.loc[( df['day_of_week'] == 'Mon'), 'attendance'].sum()
        die = dec.loc[(df['day_of_week'] == 'Tue'), 'attendance'].sum()
        mit = dec.loc[( df['day_of_week'] == 'Wed'), 'attendance'].sum()
        don = dec.loc[( df['day_of_week'] == 'Thu'), 'attendance'].sum()
        fre = dec.loc[( df['day_of_week'] == 'Fri'), 'attendance'].sum()
        sam = dec.loc[( df['day_of_week'] == 'Sat'), 'attendance'].sum()
        son = dec.loc[( df['day_of_week'] == 'Sun'), 'attendance'].sum()

        if mon is None:
            mon = 0
        if mon is None:
            die = 0
        if mon is None:
            mit = 0
        if mon is None:
            don = 0
        if mon is None:
            fre = 0
        if mon is None:
            sam = 0
        if mon is None:
            son = 0

        if tot > 0:
            mo.append(mon / tot * 100)
            di.append(die / tot * 100)
            mi.append(mit / tot * 100)
            do.append(don / tot * 100)
            fr.append(fre / tot * 100)
            sa.append(sam / tot * 100)
            so.append(son / tot * 100)
            mi_bot.append((mon + die) / tot * 100)
            do_bot.append((mon + die + mit) / tot * 100)
            fr_bot.append((mon + die + mit + don) / tot * 100)
            sa_bot.append((mon + die + mit + don + fre) / tot * 100)
            so_bot.append((mon + die + mit + don + fre + sam) / tot * 100)
            total.append(df.loc[(df['date_decade'] == current_decade), 'attendance'].sum())
        else:
            mo.append(0)
            di.append(0)
            mi.append(0)
            do.append(0)
            fr.append(0)
            sa.append(0)
            so.append(0)
            mi_bot.append(0)
            do_bot.append(0)
            fr_bot.append(0)
            sa_bot.append(0)
            so_bot.append(0)
        count.append(current_decade)

    plt.bar(count,mo, color = 'r')
    plt.bar(count,di,bottom=mo)
    plt.bar(count, mi, bottom= mi_bot)
    plt.bar(count, do, bottom=do_bot)
    plt.bar(count, fr, bottom=fr_bot)
    plt.bar(count, sa, bottom=sa_bot)
    plt.bar(count, so, bottom=so_bot)
    plt.xlabel("decade")
    plt.ylabel("attendance per weekday in %")
    plt.legend(["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"],bbox_to_anchor=(1.02, 1),loc = 'upper left')
    plt.title("What Weekday is the most popular?")

def weekday_games(df):
    decades = np.unique(df[['date_decade']].values.ravel())

    mo = []
    di = []
    mi_bot = []
    mi = []
    do_bot = []
    do = []
    fr_bot = []
    fr = []
    sa_bot = []
    sa = []
    so_bot = []
    so = []
    total = []
    i = 1
    count = []
    for current_decade in decades:
        dec =  df.loc[(df['date_decade'] == current_decade)]
        tot = df[(df['date_decade'] == current_decade)].groupby('date_decade').size().get(current_decade)
        mon = dec[( df['day_of_week'] == 'Mon')].groupby('day_of_week').size().get('Mon')
        die = dec[(df['day_of_week'] == 'Tue')].groupby('day_of_week').size().get('Tue')
        mit = dec[( df['day_of_week'] == 'Wed')].groupby('day_of_week').size().get('Wed')
        don = dec[( df['day_of_week'] == 'Thu')].groupby('day_of_week').size().get('Thu')
        fre = dec[( df['day_of_week'] == 'Fri')].groupby('day_of_week').size().get('Fri')
        sam = dec[( df['day_of_week'] == 'Sat')].groupby('day_of_week').size().get('Sat')
        son = dec[( df['day_of_week'] == 'Sun')].groupby('day_of_week').size().get('Sun')

        mo.append(mon / tot * 100)
        di.append(die / tot * 100)
        mi.append(mit / tot * 100)
        do.append(don / tot * 100)
        fr.append(fre / tot * 100)
        sa.append(sam / tot * 100)
        so.append(son / tot * 100)
        mi_bot.append((mon + die) / tot * 100)
        do_bot.append((mon + die + mit) / tot * 100)
        fr_bot.append((mon + die + mit + don) / tot * 100)
        sa_bot.append((mon + die + mit + don + fre) / tot * 100)
        so_bot.append((mon + die + mit + don + fre + sam) / tot * 100)
        total.append(df.loc[(df['date_decade'] == current_decade), 'attendance'].sum())

        count.append(current_decade)


    plt.bar(count,mo, color = 'r')
    plt.bar(count,di,bottom=mo)
    plt.bar(count, mi, bottom= mi_bot)
    plt.bar(count, do, bottom=do_bot)
    plt.bar(count, fr, bottom=fr_bot)
    plt.bar(count, sa, bottom=sa_bot)
    plt.bar(count, so, bottom=so_bot)

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

    for current_courts in courts:
        #home_games_won = df.loc[(df['park_id'] == current_courts), 'h_score'].sum()
        home_games_won = df[(df['park_id'] == current_courts) & (df['h_score'] > df['v_score'])] \
            .groupby('park_id') \
            .size() \
            .to_dict()
        home_games_won = home_games_won.get(current_courts)
        attendance = df.loc[(df['park_id'] == current_courts), 'attendance'].mean()

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

            if res >= 5.0:
                print(current_courts)
                print(f"quota :  {res}")
                print(home_games_won + visiting_games_won)

            if home_games_won > 2700:
                home_win_label.append(home_games_won)
                visit_win_label.append(visiting_games_won)
                names_label.append(current_courts)

        #merged_wins = {key: home_games_won.get(key, 0) / visiting_games_won.get(key, 0)
                      # for key in set(home_games_won) | set(visiting_games_won)}

    plt.scatter( visit_win,home_win, c = visiters , cmap = "Greens")
    plt.plot([0,3000],[0,3000])
    for name,x,y in zip(names_label,visit_win_label,home_win_label):

        plt.annotate(name, (x,y))