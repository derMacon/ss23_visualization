import matplotlib.pyplot as plt


def plot_v_score_count(df):
    df = df.sort_values(["v_score"])
    df = df.drop(df[df.v_score > 20].index)
    # df['v_score'] = df['v_score'].quantile(0.1) # TODO use quantile syntax
    plt.hist2d(df['date_year'], df['v_score'])

    means_v_score = df.groupby(['date_year'])['v_score'].mean()
    plt.plot(means_v_score.keys(), means_v_score, color='red', label='mean')
    plt.title('visiting score')
    plt.legend()
    plt.show()
