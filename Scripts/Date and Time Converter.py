from astropy.time import Time
from astropy.time import Time


def mjd_to_utc(mjd_value):
    time_mjd = Time(mjd_value, format='mjd')
    time_utc = time_mjd.utc.iso
    return time_utc


# Example usage:
mjd_value = 59561.0 # Replace with your MJD value
utc_time = mjd_to_utc(mjd_value)
print(f"MJD {mjd_value} corresponds to UTC: {utc_time}")

from astropy.time import Time

def jd_to_utc(jd):
    # Create an Astropy Time object from Julian Date (JD)
    t = Time(jd, format='jd', scale='utc')

    # Convert to ISO format UTC
    utc_time = t.utc.iso

    return utc_time


# Example usage:
if __name__ == "__main__":
    jd_value = 2457120  # Replace with your Julian Date value
    utc_time = jd_to_utc(jd_value) #add this number to get utc
    #print(f"Julian Date {jd_value} corresponds to UTC time: {utc_time}")

