import urllib
import json
import time
import ssl
import csv
import numpy as np
import pandas as pd

# If you are in China use this URL:
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
apikey = "&key=AIzaSyBUIDQg5zs2VfotIlrkwsfUjPburQuSbD4"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

zips = list()
places = set()

#columns = ['division', 'line', 'station_name', 'zip_code']
#df = pf.DataFrame(columns=columns)

with open('StationEntrances.csv', 'rb') as fh:
    reader = csv.reader(fh)
    next(reader)
    for row in reader:
        division = row[0].upper()
        line = row[1].upper()
        station_name = row[2].upper()
        lat, lng = row[3], row[4]
        place = division + line + station_name + lat + lng
        if place not in places:
            places.add(place)
            latlng = [lat + ',' + lng, ]
            url = serviceurl + 'latlng=' + str(latlng[0]) + apikey
            uh = urllib.urlopen(url, context=scontext)
            data = uh.read()
            js = json.loads(str(data))
            zip_code = js['results'][0]['address_components'][7]['long_name']
            zips.append([division, line, station_name, zip_code])
        else:
            continue

print 'data retrieved'
#print zips

with open('zips.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',',quoting = csv.QUOTE_MINIMAL)
    for latlngzip in zips:
        writer.writerow(latlngzip)

#print zips

#40.710368,-74.009509

#https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY
#https://maps.googleapis.com/maps/api/geocode/json?lanlng=40.710368,-74.009509&key=AIzaSyBZkXtmv9aAapicnQGx4su7mqb_jWIvMUg
#https://maps.googleapis.com/maps/api/geocode/json?latlng=%28%2740.710368%27%2C+%27-74.009509%27%29&sensor=false&key=AIzaSyBZkXtmv9aAapicnQGx4su7mqb_jWIvMUg
