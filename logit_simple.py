import math

import matplotlib.pyplot as plt
import pandas as pd

# Use Logit before STL to increase the efficiency of the Trend isolation


df = pd.read_csv('data/monthly-milk-production-pounds.csv', names=['Month', 'Data'], parse_dates=True)
df['Month'] = pd.to_datetime(df['Month'])

ser = df['Data']
min_ = ser.min() - 1
max_ = ser.max() + 1


df['Logit'] = ser.map(lambda x: math.log((x-min_) / (max_-x), 2))
df = df.set_index('Month')      # df.reset_index(inplace=True)


df.plot()
plt.show()

