import matplotlib.pyplot as plt
import numpy as np

def teams_v_score(df):
    df = df.sort_values(["v_score"])

    threshold = df['v_score'].quantile(0.99)
    df = df.drop(df[df['v_score'] > threshold].index)
    plt.hist2d(df['date_year'], df['v_score'])

    means_v_score = df.groupby(['date_year'])['v_score'].mean()
    plt.plot(means_v_score.keys(), means_v_score, color='red', label='mean')
    plt.title('visiting score')
    plt.legend()
