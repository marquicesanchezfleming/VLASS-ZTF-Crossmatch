import re
import math

def parse_line(line):
    match = re.match(r'(ZTF\d+[a-z]+)_VLASS(\d\.\d).+peak flux of ([\d.]+) and a RMS of ([\d.]+)', line)
    if match:
        return match.groups()
    return None


def significnce_calculatorv2(data):
    results = []
    for name, epochs in data.items():
        if len(epochs) >= 2:
            epoch1 = epochs[0]
            epoch2 = epochs[1]
            deltapf12 = round(float(epoch2[1]) - float(epoch1[1]), 3)
            trms12 = math.sqrt(float(epoch1[2]) ** 2 + float(epoch2[2]) ** 2)
            sigma1 = deltapf12 / trms12

            if len(epochs) >= 3:
                epoch3 = epochs[2]
                deltapf23 = round(float(epoch3[1]) - float(epoch2[1]), 3)
                trms23 = math.sqrt(float(epoch2[2]) ** 2 + float(epoch3[2]) ** 2)
                sigma2 = deltapf23 / trms23
                results.append((name, sigma1, sigma2))
            else:
                results.append((name, sigma1, None))
        else:
            results.append((name, None, None))  # Handle cases with less than 2 epochs

    return results


input_path = '/Fluxes_and_RMS.csv'
data = {}
with open(input_path, 'r') as file:
    for line in file:
        parsed = parse_line(line)
        if parsed:
            name, epoch, peak_flux, rms = parsed
            if name not in data:
                data[name] = []
            data[name].append((epoch, peak_flux, rms))

results = significnce_calculatorv2(data)

output_path = '/2nd_Cut_Material/Calculated_Significanes.csv'
with open(output_path, 'w') as file:
    for name, sigma1, sigma2 in results:
        if sigma1 is not None:
            if sigma2 is not None:
                file.write(f"{name} has a 1-2 Significance of {sigma1} and a 2-3 Significance of {sigma2}\n")
            else:
                file.write(f"{name} has a 1-2 Significance of {sigma1} and no 2-3 Significance due to missing epoch\n")
        else:
            file.write(f"{name} has no 1-2 Significance due to missing epochs\n")

