from toolz import pipe

from api.weather_api import make_city_url, get_city_data, get_cities_weather, read_from_file
from model.Location import Location
from model.mission import Mission
from repository.json_repository import read_from_file
from service.distance_service import haversine_distance, current_location
from service.location_service import extract_location_from_json
from service.score_service import calculate_score
from service.weather_service import extract_weather_from_json


def make_all_missions(targets, pilots, aircrafts, weathers, locations):
    missions = []
    for target in targets:
        for pilot in pilots:
            for aircraft in aircrafts:
                missions.append(make_mission(target, pilot, aircraft, weathers, locations))
    return missions

def make_mission(target, pilot, aircraft, weathers, locations):
    target_loc :Location = pipe(
        # make_city_url("Location", target.city, "a85d2becf7d27312f6d42c5a3d9adccf"),
        # get_city_data,
        #read_from_file("assets/cities_api_data/cities_locations.json")[target.city],
        locations[target.city],
        extract_location_from_json
    )
    distance = haversine_distance(target_loc.lat, target_loc.lon, current_location.lat, current_location.lon)
    weather_condition = pipe(
        # make_city_url("Weather","Beirut", "a85d2becf7d27312f6d42c5a3d9adccf"),
        # get_city_data,
        #read_from_file("assets/cities_api_data/cities_weather.json")[target.city],
        weathers[target.city],
        extract_weather_from_json
    )

    mission_fit_score = calculate_score(
        pilot=pilot,
        target=target,
        aircraft=aircraft,
        weather=weather_condition,
        distance=distance
    )

    return Mission(
        target_city=target.city,
        priority=target.priority,
        assigned_pilot=pilot.name,
        assigned_aircraft=aircraft.type,
        distance=distance,
        weather_condition=weather_condition,
        pilot_skill=pilot.skill,
        aircraft_speed=aircraft.speed,
        fuel_capacity=aircraft.fuel_capacity,
        missin_fit_score= mission_fit_score
    )