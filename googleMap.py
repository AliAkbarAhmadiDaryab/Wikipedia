import json
import urllib.request, urllib.parse, urllib.error
import folium
from dict_correspondent import read_list
urlservie = "https://maps.googleapis.com/maps/api/geocode/json?"
locations = read_list('targetprovinces/2019/April.txt')
location_address = {}
api_key ='A_ovfo7asdf1232=+_qZYHiO-3L1DDDqsC8849583jRWPlw8Kfto'

for location in locations:
    url = urlservie + urllib.parse.urlencode({'address': location})+ '&'+ urllib.parse.urlencode({'key':api_key})
    print('Retrieving,... {0}'.format(location))
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print(data['results'])
    try:
        js_data = json.loads(data)
    except:
        js = None

    lat = js_data['results'][0]['geometry']['location']['lat']
    lng = js_data['results'][0]['geometry']['location']['lng']
    location_address[location] = [lat, lng]


print(location_address)

m = folium.Map(location= [33.828362,65.208463], zoom_start=15)
m