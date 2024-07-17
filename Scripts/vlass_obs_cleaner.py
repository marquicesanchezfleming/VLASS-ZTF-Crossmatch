import pandas as pd

# Load the CSV file
file_path = "/CSV's/VLASS_Observations.csv"
df = pd.read_csv(file_path)

# Sort the DataFrame alphabetically by all columns and drop duplicates
sorted_df = df.sort_values(by=list(df.columns)).drop_duplicates()

# Save the cleaned and sorted DataFrame to a new CSV file
cleaned_file_path = '/cleaned_vlass_obs.csv'
sorted_df.to_csv(cleaned_file_path, index=False)

