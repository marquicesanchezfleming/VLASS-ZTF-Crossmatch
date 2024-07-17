from astropy.time import Time
from astropy.time import Time


def mjd_to_utc(mjd_value):
    time_mjd = Time(mjd_value, format='mjd')
    time_utc = time_mjd.utc.iso
    return time_utc


# Example usage:
mjd_value = 58214.244317 # Replace with your MJD value
utc_time = mjd_to_utc(mjd_value)
print(f"MJD {mjd_value} corresponds to UTC: {utc_time}")

