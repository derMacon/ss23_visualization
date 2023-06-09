import numpy as np
import pandas as pd

header_line = "x,date,state"
dtypeDict={"x": np.int32, "date": str, "state": str}
df = pd.read_csv('../datasets/test/test.csv', sep=',', dtype=dtypeDict)

date_array = np.array(df['date'], dtype='datetime64[D]')
print(date_array)

# print(df['date'])
# print(df.values)

# dataFull=pd.read_csv("data/WPP2022_Demographic_Indicators_Medium.csv",sep=",",dtype=dtypeDict)
