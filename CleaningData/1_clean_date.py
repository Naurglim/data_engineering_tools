import pandas as pd
import datetime as dt
from DataSets.datasets import get_dataset


## Fix date data -> set today as default for data in the future.
ride_sharing = get_dataset('rides','3')

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'], format='mixed').dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())