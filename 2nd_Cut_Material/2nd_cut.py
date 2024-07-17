import csv
import re
def filter_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            line = row[0]
            numbers = re.findall(r"Significance of (-?[\d\.]+)", line)
            numbers = [float(num) for num in numbers]
            if any(num > 4 or num < -4 for num in numbers):
                writer.writerow(row)

input_file = '/2nd_Cut_Material/Calculated_Significanes.csv'
output_file = '/2nd_Cut_Material/2nd_cut_candidates.csv'
filter_csv(input_file, output_file)
