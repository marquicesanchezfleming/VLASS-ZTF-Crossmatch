import pandas as pd
import re

# Load the CSV file
csv_file_path = '/Difference_in_Days.csv'
df = pd.read_csv(csv_file_path)

# Extract the column name
column_name = df.columns[0]

# Define a regular expression pattern to match the entries
pattern = r'^(ZTF[\w]+)_VLASS([\d.]+v\d+|[\d.]+) has a difference in days of ([-\d.]+)$'

# Extract the relevant information
parsed_data = df[column_name].str.extract(pattern)
parsed_data.columns = ['ZTF Object', 'VLASS Epoch', 'Difference in Days']

# Convert the parsed data to a list of dictionaries
data_list = parsed_data.to_dict('records')

