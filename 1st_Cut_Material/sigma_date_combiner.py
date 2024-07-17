import csv

# Input file names
file1 = '/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/Semi_Chosen_Ones.csv'
file2 = "/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/CSV's/Difference_in_Days.csv"
output_file = 'combined.csv'

# Read the first CSV file into a dictionary
data1 = {}
with open(file1, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0:
            continue
        name_value = row[0].split(' is ')
        name = name_value[0].replace('.png', '')  # remove '.png' to match with the second file
        value = float(name_value[1])
        data1[name] = value

# Read the second CSV file into a dictionary
data2 = {}
with open(file2, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0:
            continue
        name_value = row[0].split(' has a difference in days of ')
        name = name_value[0]
        diff_days = float(name_value[1])
        data2[name] = diff_days

# Combine the data from both dictionaries
combined_data = []
for name, value in data1.items():
    if name in data2:
        combined_data.append(f'{name}_VLASS.png is {value} and has a difference in days of {data2[name]}')
    else:
        combined_data.append(f'{name}_VLASS.png is {value} and Date not found')

# Write the combined data to the output CSV file
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    for item in combined_data:
        writer.writerow([item])

print(f'Combined data has been written to {output_file}')
