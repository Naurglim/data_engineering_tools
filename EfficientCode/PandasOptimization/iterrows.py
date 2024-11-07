import pandas as pd

# 1:
"""
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. 
But, what does this mean? Let's explore with a few coding exercises.
A pandas DataFrame has been loaded into your session called pit_df. 
This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012.
"""

# Data:
pit_df = pd.DataFrame()  # pittsburg data
"""
  Team League  Year   RS   RA   W    G  Playoffs
0  PIT     NL  2012  651  674  79  162         0
1  PIT     NL  2011  610  712  72  162         0
2  PIT     NL  2010  587  866  57  162         0
3  PIT     NL  2009  636  768  62  161         0
4  PIT     NL  2008  735  884  67  162         0
"""

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)


# 2:
"""
You've been hired by the San Francisco Giants as an analyst—congrats! 
The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. 
This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 
'RS' means runs scored and 'RA' means runs allowed.
"""

# data:
giants_df = pd.DataFrame()
"""
  Team League  Year   RS   RA   W    G  Playoffs
0  SFG     NL  2012  718  649  94  162         1
1  SFG     NL  2011  570  578  86  162         0
2  SFG     NL  2010  697  583  92  162         1
3  SFG     NL  2009  657  611  88  162         0
4  SFG     NL  2008  640  759  72  162         0
"""

# Providec func:
def calc_run_diff(runs_scored, runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff


# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)