from astropy.cosmology import Planck18
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.image as mpimg
import csv

z = (0.0175)

dL = Planck18.luminosity_distance(z).cgs.value

mjy = (5.57)
Jy = np.array(mjy) * 10**-3

flux_conversion = 1e-23
flux = Jy * flux_conversion

Luminosity = 4 * np.pi * dL**2 * flux

print(Luminosity)

input_file = "/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/CSV's/smallest_values_over_100.csv"
values = []

with open(input_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        value = float(row[1])
        values.append(value)

plt.figure(figsize=(10, 6))
plt.hist(values, bins=20, color='skyblue', edgecolor='black')
plt.title('Total of 804 Transients')
plt.xlabel('Shortest dt from peak optical')
plt.ylabel('Number of Transients')
plt.grid(axis='y', alpha=0.75)
plt.axvline(x=0, color='red', linestyle='--')

input_file = "/Users/Djslime07/Documents/GitHub/VLASS-ZTF-Crossmatch/CSV's/largest_values_over_100.csv"
values = []

with open(input_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        value = float(row[1])
        values.append(value)

plt.figure(figsize=(10, 6))
plt.hist(values, bins=20, color='skyblue', edgecolor='black')
plt.title('Total of 6720 Transients')
plt.xlabel('Largest dt from peak optical')
plt.ylabel('Number of Transients')
plt.grid(axis='y', alpha=0.75)
plt.axvline(x=0, color='red', linestyle='--')

#plt.show()


