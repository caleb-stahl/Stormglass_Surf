
"""
Attempting to make an API Call
"""
# 34.407703, -119.879725
import pprint
import arrow
import requests
import math

def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

response = requests.get(
    url = 'https://api.stormglass.io/v2/weather/point',
    params = {'lat' : 34.407703, #Sands Beach
              'lng' : -119.879725,
              'params' : 'waveHeight',
              'start' : arrow.utcnow().shift(hours = -1).to('UTC').timestamp(), #start time 1 hour ago
              'end' : arrow.utcnow().to('UTC').timestamp() #end time is current time
              },
    headers = {'Authorization' : '78a5a572-e24d-11ed-8b7f-0242ac130002-78a5a5d6-e24d-11ed-8b7f-0242ac130002' })


the_data = response.json()

pprint.pprint(the_data)

# mal_data = {'hours': [{'time': '2023-04-24T03:00:00+00:00',
#             'waveHeight': {'icon': 2.31, 'noaa': 1.59, 'sg': 2.31}},
#            {'time': '2023-04-24T04:00:00+00:00',
#             'waveHeight': {'icon': 2.27, 'noaa': 1.61, 'sg': 2.27}}],
#  'meta': {'cost': 1,
#           'dailyQuota': 10,
#           'end': '2023-04-24 04:01',
#           'lat': 34.407703,
#           'lng': -119.879725,
#           'params': ['waveHeight'],
#           'requestCount': 3,
#           'start': '2023-04-24 03:00'}}

# icon = mal_data['hours'][0]['waveHeight']['icon']
# noaa = mal_data['hours'][0]['waveHeight']['noaa']
# sg = icon = mal_data['hours'][0]['waveHeight']['sg']
# avg = (icon + noaa + sg) / 3
# print(meters_to_feet(icon), 'icon')
# print(meters_to_feet(noaa), 'noaa')
# print(meters_to_feet(sg), 'sg')