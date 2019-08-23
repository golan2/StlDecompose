import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Seasonal decomposition using moving averages

df = pd.read_csv('data/monthly-milk-production-pounds.csv', names=['Month', 'data'], parse_dates=True)
df['Month'] = pd.to_datetime(df['Month'])   # , errors='coerce'
df.set_index('Month')
res = seasonal_decompose(df['data'], model='additive', freq=4)
res.plot()
plt.show()

