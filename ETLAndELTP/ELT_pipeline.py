import pandas as pd

"""
Feeling pretty good about running ETL processes? Well, it's time to give ELT pipelines a try. 
Like before, the extract(), load(), and transform() functions have been defined for you; 
all you'll have to worry about is running these functions. Good luck!
"""
def extract(file_name):
    print(f"Extracting data from {file_name}.")
    return pd.read_csv(file_name)


def load(data_frame, table_name):
    print(f"Loading cleaned data to {table_name}.")
    data_warehouse.load_table(data_frame, table_name)


# Complete building the transform() function
def transform(source_table, target_table):
  data_warehouse.execute(f"""
  CREATE TABLE {target_table} AS
      SELECT
          CONCAT("Product ID: ", product_id),
          quantity * price
      FROM {source_table};
  """)

extracted_data = extract(file_name="raw_sales_data.csv")
load(data_frame=extracted_data, table_name="raw_sales_data")

# Populate total_sales by transforming raw_sales_data
transform(source_table="raw_sales_data", target_table="total_sales")
