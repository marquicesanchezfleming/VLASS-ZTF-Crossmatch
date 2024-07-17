import csv

input_file = "/1st_Cut_Material/combined.csv"
output_file = "/1st_Cut_Material/1st_cut_candidates.csv"

def is_valid_line(line):
    try:
        # Extract the difference in days from the line
        parts = line.split(' has a difference in days of ')
        diff_days = float(parts[1])
        return diff_days > 0
    except:
        return False

# Read the input CSV and filter lines
filtered_data = []
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0:
            continue
        if is_valid_line(row[0]):
            filtered_data.append(row[0])

# Write the filtered data to the output CSV file
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    for item in filtered_data:
        writer.writerow([item])

print(f'Filtered data has been written to {output_file}')