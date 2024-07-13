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
            if any(num > 2 or num < -2 for num in numbers):
                writer.writerow(row)

input_file = '/Users/Djslime07/PycharmProjects/Rewriting /Calculated_Significances.csv'
output_file = '/Users/Djslime07/PycharmProjects/Rewriting /The_Chosen_Ones.csv'
filter_csv(input_file, output_file)
