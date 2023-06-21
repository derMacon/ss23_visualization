from game_log_importer import read_game_logs as game_logs
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


df = game_logs()
print(df.shape)

# for curr_date in df['date']:
#     datetime_obj = datetime.strptime(curr_date, '%Y%m%d')
#     df['date'] = np.datetime64(datetime_obj, 'D')

df['date'] = df['date'].apply(lambda x: int(np.datetime64(datetime.strptime(str(x), '%Y%m%d'), 'Y').astype(object).year))
print(df['date'])


print('mean: ', df.groupby(['date'])['v_score'].mean())

means_v_score = df.groupby(['date'])['v_score'].mean()
print('mean shape: ', means_v_score.shape)
print('year shape: ', df['date'].shape)

# print(df['v_score'])
# df = df.sort_values(["v_score"])
# df = df.drop(df[df.v_score > 20].index)
# plt.hist2d(df['date'], df['v_score'])

plt.plot(range(42), means_v_score)


plt.show()


