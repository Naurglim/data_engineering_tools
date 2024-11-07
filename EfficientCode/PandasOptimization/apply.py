import pandas as pd

# apply (like map)
"""
The Tampa Bay Rays want you to analyze their data.

They'd like the following metrics:

The sum of each column in the data
The total amount of runs scored in a year ('RS' + 'RA' for each year)
The 'Playoffs' column in text format rather than using 1's and 0's
"""

def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 

rays_df = pd.DataFrame()
"""
       RS   RA   W  Playoffs
2012  697  577  90         0
2011  707  614  91         1
2010  802  649  96         1
2009  803  754  84         0
2008  774  671  97         1
"""

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)


# 2
"""
Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. 
They'd like for you to help settle a debate amongst the managers. 
One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. 
Another manager says this is not true.

Let's use the below function and the .apply() method to see which manager is correct.
"""
import numpy as np

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

dbacks_df = pd.DataFrame()
"""
   Team League  Year   RS   RA    W    G  Playoffs
0   ARI     NL  2012  734  688   81  162         0
1   ARI     NL  2011  731  662   94  162         1
2   ARI     NL  2010  713  836   65  162         0
3   ARI     NL  2009  720  782   70  162         0
4   ARI     NL  2008  720  706   82  162         0
5   ARI     NL  2007  712  732   90  162         1
6   ARI     NL  2006  773  788   76  162         0
7   ARI     NL  2005  696  856   77  162         0
8   ARI     NL  2004  615  899   51  162         0
9   ARI     NL  2003  717  685   84  162         0
10  ARI     NL  2002  819  674   98  162         1
11  ARI     NL  2001  818  677   92  162         1
12  ARI     NL  2000  792  754   85  162         0
13  ARI     NL  1999  908  676  100  162         1
14  ARI     NL  1998  665  812   65  162         0
"""

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

