import pandas as pd

# Define the input and output file paths
input_file = "/Difference_in_Days.csv"
output_file = '/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/fixed_obs?.csv'  # Replace with your output file path

# Read the input CSV file
with open(input_file, 'r') as f:
    lines = f.readlines()

# Process the lines to extract the required data
data = []
for line in lines:
    # Split the line at the first occurrence of " has a difference in days of "
    parts = line.strip().split(' has a difference in days of ')
    if len(parts) == 2:
        ztf_object = parts[0]
        difference = float(parts[1])
        data.append((ztf_object, difference))

# Create a DataFrame
df = pd.DataFrame(data, columns=['ZTF_Object', 'Difference_in_Days'])

# Save the DataFrame to a new CSV file
df.to_csv(output_file, index=False)
