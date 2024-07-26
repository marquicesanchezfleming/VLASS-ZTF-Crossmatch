import pandas as pd

input_file = '/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/boink.csv'  # Replace with your input file path
df = pd.read_csv(input_file, delimiter='|')

# Remove the 'Display all params' column
df_cleaned = df.drop(columns=['Display all params'])

# Save the cleaned data to a new CSV file
output_file = 'cleaned_file.csv'  # Replace with your desired output file path
df_cleaned.to_csv(output_file, index=False)
