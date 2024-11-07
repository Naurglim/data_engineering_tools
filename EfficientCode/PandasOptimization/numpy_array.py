import pandas as pd
import numpy as np

"""
Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. 
You'll revisit the win percentage calculations you performed row by row with the .iloc method:

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list
Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.
"""

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

baseball_df = pd.DataFrame()
"""
     Team League  Year   RS   RA    W    G  Playoffs
0     ARI     NL  2012  734  688   81  162         0
1     ATL     NL  2012  700  600   94  162         1
2     BAL     AL  2012  712  705   93  162         1
3     BOS     AL  2012  734  806   69  162         0
4     CHC     NL  2012  613  759   61  162         0
...   ...    ...   ...  ...  ...  ...  ...       ...
1227  PHI     NL  1962  705  759   81  161         0
1228  PIT     NL  1962  706  626   93  161         0
1229  SFG     NL  1962  878  690  103  165         1
1230  STL     NL  1962  774  664   84  163         0
1231  WSA     AL  1962  599  716   60  162         0
"""

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())


# 2
"""
A pandas DataFrame (baseball_df) has been loaded into your session. 
For convenience, a dictionary describing each column within baseball_df has been printed into your console. 
You can reference these descriptions throughout the exercise.

You'd like to attempt to predict a team's win percentage for a given season by using the team's 
total runs scored in a season ('RS') and total runs allowed in a season ('RA') with the following function:

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)
Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.
"""

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

baseball_df = pd.DataFrame()
"""
     Team League  Year   RS   RA    W    G  Playoffs    WP
0     ARI     NL  2012  734  688   81  162         0  0.50
1     ATL     NL  2012  700  600   94  162         1  0.58
2     BAL     AL  2012  712  705   93  162         1  0.57
3     BOS     AL  2012  734  806   69  162         0  0.43
4     CHC     NL  2012  613  759   61  162         0  0.38
...   ...    ...   ...  ...  ...  ...  ...       ...   ...
1227  PHI     NL  1962  705  759   81  161         0  0.50
1228  PIT     NL  1962  706  626   93  161         0  0.58
1229  SFG     NL  1962  878  690  103  165         1  0.62
1230  STL     NL  1962  774  664   84  163         0  0.52
1231  WSA     AL  1962  599  716   60  162         0  0.37
"""
"""
OrderedDict([('Team', 'Abbreviated team name'),
             ('League', 'Specifies National League or American League'),
             ('Year', "Each season's year"),
             ('RS', 'Runs scored in a season'),
             ('RA', 'Runs allowed in a season'),
             ('W', 'Wins in a season'),
             ('G', 'Games played in a season'),
             ('Playoffs', '`1` if a team made the playoffs; `0` if they did not'),
             ('WP', 'True win percentage for a season')])
"""


# step 1
"""
Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. 
Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.
"""

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)


# step 2
"""
Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. Save the predicted win percentage as win_perc_preds_apply.
"""
# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)


# step 3
"""
Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). 
Save these predictions as win_perc_preds_np.
"""
# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())


