import matplotlib.pyplot as plt
import pandas as pd
from stldecompose import decompose

# Seasonal decomposition using Loess

df = pd.read_csv('data/monthly-milk-production-pounds.csv', names=['Month', 'Data'], parse_dates=True)
df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index('Month')

res = decompose(df, 12)

df['seasonal'] = res.__getattribute__('seasonal')
df['trend'] = res.__getattribute__('trend')
df['Data'] = 0
df['tren_seas'] = df['seasonal'] + df['trend']

df.plot()
plt.show()
