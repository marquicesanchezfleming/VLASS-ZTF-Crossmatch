from astropy.time import Time

def mjd_to_utc(mjd_value):
    time_mjd = Time(mjd_value, format='mjd')
    time_utc = time_mjd.utc.iso
    return time_utc

# List of MJD values
mjd_values = [
59483.0
]

# Convert each MJD to UTC
utc_times = [mjd_to_utc(mjd) for mjd in mjd_values]

# Print the UTC times
for mjd, utc in zip(mjd_values, utc_times):
    print(f'UTC: {utc}')

