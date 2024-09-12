from os import stat_result


from api.weather_api import get_cities_weather
from repository.csv_repository1 import write_missions_to_csv

from repository.json_repository import read_target_from_json, read_pilot_from_json, \
    read_aircraft_from_json

from service.mission_sevice import make_all_missions, get_top_7_missions

if __name__ == '__main__':

    #get city Location from api
    # pipe(
    #     make_city_url("Location","Gaza", "a85d2becf7d27312f6d42c5a3d9adccf"),
    #     get_city_data,
    #     write_to_file("assets/cities_api_data/Gaza City_location.json")
    # )

    # #get city weather from api
    # pipe(
    #     make_city_url("Weather","Beirut", "a85d2becf7d27312f6d42c5a3d9adccf"),
    #     get_city_data,
    #     write_to_file("assets/cities_api_data/beirut_weather.json")
    # )

    targets = read_target_from_json("assets/targets_data.json")
    pilots = read_pilot_from_json("assets/pilots_data.json")
    aircrafts = read_aircraft_from_json("assets/aircraft_data.json")

    weathers = get_cities_weather("Weather")
    locations = get_cities_weather("Location")

    missions = make_all_missions(targets, pilots, aircrafts, weathers, locations)
    write_missions_to_csv(missions, "all_missions.csv")
    li = get_top_7_missions(missions)
    write_missions_to_csv(li, "top_seven.csv")
