import matplotlib.pyplot as plt
import numpy as np

def attendance_per_year(df):
    df = df[df['attendance'].notna()]

    means_v_score = df.groupby(['date_year'])['attendance'].mean().to_dict()
    means_v_score = {str(key): value for key, value in means_v_score.items()}

    print('means_v_score: ', means_v_score)

    plt.plot(means_v_score.keys(), means_v_score.values(), color='red', label='mean')
    plt.title('attendance')
    plt.legend()


def attendance_per_decade(df):
    df = df[df['attendance'].notna()]

    means_v_score = df.groupby(['date_decade'])['attendance'].mean().to_dict()
    means_v_score = {str(key): value for key, value in means_v_score.items()}

    # TODO
    plt.scatter(means_v_score.keys(), means_v_score.values(), color='red', label='mean')
    plt.title('attendance')
    plt.legend()


def data_per_year(df):
    data_per_year = df.groupby(['date_year']).size()
    plt.plot(data_per_year)


def data_per_decade(df):
    data_per_decade = df.groupby(['date_decade']).size()
    plt.plot(data_per_decade)


