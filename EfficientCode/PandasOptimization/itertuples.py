import pandas as pd

"""
Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. 
You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.

A pandas DataFrame has been loaded into your session called rangers_df. 
This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') 
for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').
"""

rangers_df = pd.DataFrame()

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Tear
    wins = row.W
    print(i, year, wins)
  
    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)


# 2:
# Differentials:
"""
The New York Yankees have made a trade with the San Francisco Giants for your analyst contract— you're a hot commodity! 
Your new boss has seen your work with the Giants and now wants you to do something similar with the Yankees data. 
He'd like you to calculate run differentials for the Yankees from the year 1962 to the year 2012 and find which season they had the best run differential.
"""

yankees_df = pd.DataFrame()
"""
   Team League  Year   RS   RA    W    G  Playoffs
0   NYY     AL  2012  804  668   95  162         1
1   NYY     AL  2011  867  657   97  162         1
2   NYY     AL  2010  859  693   95  162         1
3   NYY     AL  2009  915  753  103  162         1
4   NYY     AL  2008  789  727   89  162         0
5   NYY     AL  2007  968  777   94  162         1
6   NYY     AL  2006  930  767   97  162         1
7   NYY     AL  2005  886  789   95  162         1
8   NYY     AL  2004  897  808  101  162         1
9   NYY     AL  2003  877  716  101  163         1
10  NYY     AL  2002  897  697  103  161         1
11  NYY     AL  2001  804  713   95  161         1
12  NYY     AL  2000  871  814   87  161         1
13  NYY     AL  1999  900  731   98  162         1
14  NYY     AL  1998  965  656  114  162         1
15  NYY     AL  1997  891  688   96  162         1
16  NYY     AL  1996  871  787   92  162         1
17  NYY     AL  1993  821  761   88  162         0
18  NYY     AL  1992  733  746   76  162         0
19  NYY     AL  1991  674  777   71  162         0
20  NYY     AL  1990  603  749   67  162         0
21  NYY     AL  1989  698  792   74  161         0
22  NYY     AL  1988  772  748   85  161         0
23  NYY     AL  1987  788  758   89  162         0
24  NYY     AL  1986  797  738   90  162         0
25  NYY     AL  1985  839  660   97  161         0
26  NYY     AL  1984  758  679   87  162         0
27  NYY     AL  1983  770  703   91  162         0
28  NYY     AL  1982  709  716   79  162         0
29  NYY     AL  1980  820  662  103  162         1
30  NYY     AL  1979  734  672   89  160         0
31  NYY     AL  1978  735  582  100  163         1
32  NYY     AL  1977  831  651  100  162         1
33  NYY     AL  1976  730  575   97  159         1
34  NYY     AL  1975  681  588   83  160         0
35  NYY     AL  1974  671  623   89  162         0
36  NYY     AL  1973  641  610   80  162         0
37  NYY     AL  1971  648  641   81  162         0
38  NYY     AL  1970  680  612   93  163         0
39  NYY     AL  1969  562  587   80  162         0
40  NYY     AL  1968  536  531   83  164         0
41  NYY     AL  1967  522  621   72  163         0
42  NYY     AL  1966  611  612   70  160         0
43  NYY     AL  1965  611  604   77  162         0
44  NYY     AL  1964  730  577   99  164         1
45  NYY     AL  1963  714  547  104  161         1
46  NYY     AL  1962  817  680   96  162         1
"""

def calc_run_diff(runs_scored, runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff


run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)