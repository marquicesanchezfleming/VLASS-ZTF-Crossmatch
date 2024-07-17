import csv

# Read the CSV data
input_file = '/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/fixed_obs?.csv'
output_file = '../CSV'

# Read the lines from the input file
with open(input_file, 'r') as f:
    lines = f.readlines()

# Sort the lines alphabetically
sorted_lines = sorted(lines)

# Write the sorted lines to the output file
with open(output_file, 'w') as f:
    f.writelines(sorted_lines)

print(f"Sorted data has been written to {output_file}")