import json
import urllib.parse
import urllib.request

BASE_MAPQUEST_DIRECTION_URL = 'http://open.mapquestapi.com/directions/v2/route?'
BASE_MAPQUEST_EVELATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'
MAPQUEST_API_KEY = 'aDUajne4Gd7xora1zqQyatyW4FABKS7C'

# this function is to build the url for mapquest drection.
def build_search_url(location_lst: list) -> str:
    starting_point = location_lst[0]
    query_parameters = [
        ('key', MAPQUEST_API_KEY), 
        ('from', starting_point), 
    ]
    for location in location_lst[1:]:
        query_parameters.append(('to', location))
    return BASE_MAPQUEST_DIRECTION_URL  + urllib.parse.urlencode(query_parameters)

#this function is to get dictionaries data from url.
def get_direction_result(url: str) -> dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

#this function is to build url for mapquest elevation.
def build_elevation_url(latlng: tuple) -> str:
    query_parameters = [
        ('key', MAPQUEST_API_KEY),
        ('shapeFormat','raw'),
        ('unit','f'),
        ('latLngCollection',','.join(latlng))
    ]
    return  BASE_MAPQUEST_EVELATION_URL + urllib.parse.urlencode(query_parameters)

#this function is to get dictionaries data from url.
def get_elevation_result(url: str) -> dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

    

