import pandas as pd

file_path = '/Merged_Observations.csv'
data = pd.read_csv(file_path)

# Extract the 'name' and 'days diff' columns
extracted_data = data[['name_epoch', 'days_diff']]

# Create a new column with the desired format
extracted_data['Observation'] = extracted_data.apply(lambda row: f"{row['name_epoch']} has a difference in days of {row['days_diff']}", axis=1)

# Save the formatted data to a new CSV file
new_file_path = '/Difference_in_Days.csv'
extracted_data[['Observation']].to_csv(new_file_path, index=False)

