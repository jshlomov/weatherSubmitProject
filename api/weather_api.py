import json

import requests
from toolz import curry, pipe

from repository.json_repository import write_to_file, read_from_file


@curry
def make_request(method, url):
    response = requests.request(method, url)
    return response.json()

def make_city_url(data, city_name, key):
    if data == 'Weather':
        return f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={key}"
    if data == "Location":
        return f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}"

get_city_data = make_request('GET')


def get_cities_weather(data):
    res = {}
    all_trgets = read_from_file("assets/targets_data.json")["targets"]

    for city in list(map(lambda x: x["city"], all_trgets)):
        try:
            url = make_city_url(data, city, "a85d2becf7d27312f6d42c5a3d9adccf")
            response = requests.get(url)

            if response.status_code == 200:
                city_data = response.json()
                res[city] = city_data
            else:
                print(response.status_code)

        except Exception as e:
            print(e)
            return
    return res