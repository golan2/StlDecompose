import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import DecomposeResult
from stldecompose import decompose

# Seasonal decomposition using Loess + Sleeve

df = pd.read_csv('data/monthly-milk-production-pounds.csv', names=['Month', 'Data'], parse_dates=True)
df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index('Month')

stl: DecomposeResult = decompose(df, period=12)

original = stl.__getattribute__('observed')
trend = stl.__getattribute__('trend')
seasonality = stl.__getattribute__('seasonal')
residual = stl.__getattribute__('resid')

mean = residual.median()
std = residual.std()
amp = std*3 #residual.map(lambda x: math.fabs(x))

sleeve = trend + seasonality
df['naive_upper_bound'] = sleeve + amp
df['naive_lower_bound'] = sleeve - amp
df['residual'] = residual
df['amp'] = amp

df.plot()
plt.show()

