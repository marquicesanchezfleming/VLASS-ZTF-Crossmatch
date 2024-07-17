import csv

input_file = '../CSV'
output_file = '/largest_values_over_100.csv'

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        try:
            value = float(row[1])
            if value > -100:
                writer.writerow(row)
        except ValueError:
            print(f"Skipping row due to ValueError: {row}")

print(f"Filtered data has been written to {output_file}.")
