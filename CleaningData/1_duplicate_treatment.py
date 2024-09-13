import pandas as pd
import datetime as dt
from DataSets.datasets import get_dataset


## Find duplicates in data
ride_sharing = get_dataset('rides','4')
# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])


## Duplicate treatment: Drop complete duplicates, adjust for partial duplicates (duration and birth dates differ between records with same id)
# Drop complete duplicates from ride_sharing
ride_sharing = get_dataset('rides', '5')

ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby(['ride_id']).agg(statistics).reset_index()
# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0