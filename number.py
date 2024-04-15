#Program to find location and ISP
import phonenumbers

#Enter phone number
number= "+91 ##########"

from phonenumbers import geocoder
ch_num=phonenumbers.parse(number,"CH")
loc=geocoder.description_for_number(ch_num,"en")
print(loc)

from phonenumbers import carrier
service_num=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_num,"en"))

from opencage.geocoder import OpenCageGeocode
key='12476aa822014ec08c849afda90a6de1'
geocoder=OpenCageGeocode(key)
query=str(loc)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

import folium

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=loc).add_to(mymap)
mymap.save("mylocation.html")