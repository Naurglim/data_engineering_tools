import pandas as pd

"""
Here, the functions extract(), transform(), and load() have been defined for you. 
To run this data ETL pipeline, you're going to execute each of these functions. 
"""
def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_csv(file_name)


def transform(data_frame):
    print(f"Transforming {data_frame.shape[0]} rows of raw data.")
    return data_frame.loc[:, ["industry_name", "number_of_firms"]]


def load(data_frame, file_name):
    # Write cleaned_data to a CSV using file_name
    data_frame.to_csv(file_name)
    print(f"Successfully loaded data to {file_name}")


# Extract data from the raw_data.csv file
extracted_data = extract(file_name="raw_data.csv")

# Transform the extracted_data
transformed_data = transform(data_frame=extracted_data)

# Load transformed_data to the file transformed_data.csv
load(data_frame=transformed_data, file_name="transformed_data.csv")