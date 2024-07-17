import re
import csv

input_file = '/Fluxes_and_RMS.csv'
output_file = '/1st_Cut_Material/Semi_Chosen_Ones.csv'

threshold = 4.0
def process_line(line):

    match = re.match(r'(ZTF.*?\.png) has a peak flux of (\d+\.\d+) and a RMS of (\d+\.\d+)', line)
    if match:
        image_file = match.group(1)
        peak_flux = float(match.group(2))
        rms = float(match.group(3))
        value = peak_flux / rms
        if value > threshold:
            return f"{image_file} is {value}"
    return None


with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) > 0:
            line = row[0]
            result = process_line(line)
            if result:
                writer.writerow([result])

print(f"Processed data has been written to {output_file}")