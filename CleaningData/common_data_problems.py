import pandas as pd
import datetime as dt

ride_sharing = pd.DataFrame({'user_type': ['1','3','1','2','2','2'],
                            'duration': ['15 minutes', '23 minutes', '5 minutes', '35 minutes', '28 minutes','28 minutes'],
                            'tire_sizes': ['26','29','26','27','29','29'],
                            'ride_date': ['2020-01-19','2025-09-13','2020-01-19','2026-01-15','2030-10-19','2030-10-19'],
                            'ride_id': ['33','34','33','35','36','36'],
                            'user_birth_year': ['1998','1986','1998','1992','1984','1988']

                            })


# 1: get information and convert to another data type (int -> category) 
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())


# 2: clean string data and convert to another data type (string -> int)
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())


# 3: Clean category data -> assign a predefined category to some data.
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())


# 4: Fix date data -> set today as default for data in the future.
# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())


# 5: Find duplicates in data
# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])


# 6: Duplicate treatment: Drop complete duplicates, adjust for partial duplicates (duration and birth dates differ between records with same id)
# Drop complete duplicates from ride_sharing
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


