import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')
rtrList=df
rtrList

#get longitude and latitude of location by goole API
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAK-ZoGD-gB6cY1f99YFeHlVhP-xSaScCU')
lat_result=[]
lng_result=[]
for index,rtr in rtrList.iterrows():
#     Geocoding an address
    if rtr['location_chinese']!='':
        try:
            geocode_result = gmaps.geocode(rtr["location_chinese"])
            print(geocode_result[0]['geometry']['location'])
            lat_result.append(geocode_result[0]['geometry']['location']['lat'])
            lng_result.append(geocode_result[0]['geometry']['location']['lng'])
            print(rtr["location_chinese"])
#             break
            continue
        except:
            print("except location_chinese")
#     Use English addresses to supplement Chinese addresses
    if rtr['location_english']!='':
        try:
            geocode_result = gmaps.geocode(rtr["location_english"])
            print(geocode_result[0]['geometry']['location'])
            lat_result.append(geocode_result[0]['geometry']['location']['lat'])
            lng_result.append(geocode_result[0]['geometry']['location']['lng'])
            print(rtr["location_english"])
#             break
            continue
        except:
            print("except location_english")
    lat_result.append("")
    lng_result.append("")

# Put new columns to the original CSV
df['location_lat'] = lat_result
df['location_lng'] = lng_result
df.to_csv('data1122_latlng.csv', index=False)
