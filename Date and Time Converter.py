from astropy.time import Time

def mjd_to_utc(mjd):
    t = Time(mjd, format='mjd', scale='utc')
    utc_date = t.to_value('iso', subfmt='date_hms')
    return utc_date

mjd = 60474.356620
utc_date = mjd_to_utc(mjd)
print(utc_date)