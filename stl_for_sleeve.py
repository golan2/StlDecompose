from statsmodels.tsa.seasonal import DecomposeResult
from stldecompose import decompose
import pandas as pd
import plot_draw


# Using STL in order to calculate a Sleeve
#
# We run STL in order to calculate the trend and the seasonal
# Then we compose a new signal of both {trend+seasonal} which represents teh center of the sleeve.
# The sleeve's height is set to be STD * 3
# There are 2 approaches to how to calculate the STD:
# [1] Calculate STD on the entire data set. Yields a sleeve with a fixed height on all places
# [2] Calculate a moving STD at the specific location. Yields a different height in different places (depending on alpha)
#
#
# The Data
#
# The [messages-per-hour] contains number of messages in an hour.
# There is a seasonality for working hours and working days (MON-FRI).
# At '2019-07-28 15:00:00' there is an anomaly (too many messages).
# Depending on the value of alpha (for moving STD) the anomaly can be in or out of the sleeve.
#

df = pd.read_csv('data/messages-per-hour.csv', names=['Hour', 'Count'], parse_dates=True)
df['Hour'] = pd.to_datetime(df['Hour'])
df = df.set_index('Hour')

# Break down the signal into STL parts
stl: DecomposeResult = decompose(df, period=24*7, lo_frac=0.7)
original = stl.__getattribute__('observed')
trend = stl.__getattribute__('trend')
seasonality = stl.__getattribute__('seasonal')
residual = stl.__getattribute__('resid')
sleeve_center = trend + seasonality

# Fixed Height Sleeve
fixed_std = residual.std()
df['upper_bound'] = sleeve_center + fixed_std * 3
df['lower_bound'] = sleeve_center - fixed_std * 3
plot_draw.draw(df, 'df-fixed-std')

# Variant Height Sleeve (MSTD with alpha=0.05)
moving_std = residual.ewm(alpha=0.05, min_periods=20, adjust=False).std()
df['upper_bound'] = sleeve_center + moving_std * 3
df['lower_bound'] = sleeve_center - moving_std * 3
plot_draw.draw(df, 'df-moving-std-with-alpha-0.05')

# Variant Height Sleeve (MSTD with alpha=0.25)
moving_std = residual.ewm(alpha=0.25, min_periods=20, adjust=False).std()
df['upper_bound'] = sleeve_center + moving_std * 3
df['lower_bound'] = sleeve_center - moving_std * 3
plot_draw.draw(df, 'df-moving-std-with-alpha-0.25')
