import pandas as pd

"""
The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. 
Most analyses don't need all these columns. In this exercise, you will create a dataframe with fewer variables using read_csv()s usecols argument.

Let's focus on household composition to see if there are differences by geography and income level. 
To do this, we'll need columns on income group, ZIP code, tax return filing status (e.g., single or married), and dependents. 
The data uses codes for variable names, so the specific columns needed are in the instructions.
"""
# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())


"""
When working with large files, it can be easier to load and process the data in pieces. Let's practice this workflow on the Vermont tax data.
The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. 
To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, 
and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.
pandas has been imported as pd.

Instructions
100 XP
Use nrows and skiprows to make a dataframe, vt_data_next500, with the next 500 rows.
Set the header argument so that pandas knows there is no header row.
Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.
"""
vt_data_first500 = pd.DataFrame()

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header = None,
                       		  names = list(vt_data_first500))

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())


"""
When loading a flat file, pandas infers the best data type for each column. 
Sometimes its guesses are off, particularly for numbers that represent groups or qualities instead of quantities.

Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. 
The agi_stub column contains numbers that correspond to income categories, 
and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. 
Let's specify the correct data types with the dtype argument.
"""
# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub" : "category",
			  "zipcode": str}
# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())


"""
Part of data exploration and cleaning consists of checking for missing or NA values and deciding how to account for them. 
This is easier when missing values are treated as their own data type. and there are pandas functions that specifically target such NA values. 
Pandas automatically treats some values as missing, but we can pass additional NA indicators with the na_values argument. 
Here, you'll do this to ensure that invalid ZIP codes in the Vermont tax data are coded as NA.
"""
# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode": 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])


"""
In this exercise you'll use read_csv() parameters to handle files with bad data, like records with more values than columns. 
By default, trying to import such files triggers a specific error, pandas.errors.ParserError.

Some lines in the Vermont tax data here are corrupted. In order to load the good lines, we need to tell pandas to skip errors. 
We also want pandas to warn us when it skips a line so we know the scope of data issues.

Pandas has been imported as pd. The exercise code will try to read the file. 
If there is a pandas.errors.ParserError, the code in the except block will run.
"""
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines = False, 
                     warn_bad_lines = True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")