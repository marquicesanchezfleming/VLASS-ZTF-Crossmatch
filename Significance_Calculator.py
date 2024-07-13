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


input_path = '/Users/Djslime07/PycharmProjects/Rewriting /Fluxes_and_RMS.csv'
data = {}
with open(input_path, 'r') as file:
    for line in file:
        parsed = parse_line(line)
        if parsed:
            name, epoch, peak_flux, rms = parsed
            if name not in data:
                data[name] = []
            data[name].append((epoch, peak_flux, rms))

#results = significnce_calculatorv2(data)

#output_path = '/Users/Djslime07/PycharmProjects/Rewriting /Calculated_Significances.csv'
#with open(output_path, 'w') as file:
    #for name, sigma1, sigma2 in results:
        #if sigma1 is not None:
            #if sigma2 is not None:
                #file.write(f"{name} has a 1-2 Significance of {sigma1} and a 2-3 Significance of {sigma2}\n")
            #else:
                #file.write(f"{name} has a 1-2 Significance of {sigma1} and no 2-3 Significance due to missing epoch\n")
        #else:
            #file.write(f"{name} has no 1-2 Significance due to missing epochs\n")

def significnce_calculatorv1(input_path, output_path):
    deltapf23 = round(epoch3pf - epoch2pf, 3)
    deltapf12 = round(epoch2pf - epoch1pf, 3)
    trms12 = math.sqrt(epoch1rms ** 2 + epoch2rms ** 2)
    trms23 = math.sqrt(epoch2rms ** 2 + epoch3rms ** 2)
    sigma1 = deltapf12 / trms12
    deltapf23 = round(epoch3pf - epoch2pf, 3)
    deltapf12 = round(epoch2pf - epoch1pf, 3)
    trms12 = math.sqrt(epoch1rms ** 2 + epoch2rms ** 2)
    trms23 = math.sqrt(epoch2rms ** 2 + epoch3rms ** 2)
    sigma1 = deltapf12 / trms12
    sigma2 = deltapf23 / trms23

    output_file = "/Users/Djslime07/PycharmProjects/Rewriting /Calculated_Significances.csv"
    with open(output_file, 'a') as f:
        print(name, "has a 1-2 Significance of", sigma1, "and", "a 2-3 Significance of", sigma2, file=f)

epoch1pf, epoch1rms = 0.314, 0.161
epoch2pf, epoch2rms = 2.923, 0.252
epoch3pf, epoch3rms = 0.759, 0.139
name = 'ZTF20acnvniw'

input_path = '/Users/Djslime07/PycharmProjects/Rewriting /Fluxes_and_RMS.csv'
output_path = '/Users/Djslime07/PycharmProjects/Rewriting /Calculated_Significances.csv'

significnce_calculatorv1(input_path, output_path)



