from model.Aircraft import Aircraft
from model.Pilot import Pilot
from model.Target import Target
from model.Weather import Weather

def calculate_score(pilot: Pilot, target: Target, aircraft: Aircraft, weather: Weather, distance: float):
    # Calculate individual scores
    pilot_skill_score = pilot_score(pilot)  # Score based on pilot's skill
    weather_condition_score = general_weather_score(weather)  # Score based on weather condition
    priority_score_value = priority_score(target)  # Score based on target priority
    distance_fuel_score = distance_score(aircraft, distance)  # Score based on distance and fuel capacity

    # Weights for each factor
    weights = {
        "distance": 0.30,
        "priority": 0.25,
        "pilot_skill": 0.25,
        "weather_condition": 0.20,
    }

    # Calculate total score, combining all scores with their respective weights
    total_score = (
        (distance_fuel_score * weights["distance"]) +
        (pilot_skill_score * weights["pilot_skill"]) +
        (weather_condition_score * weights["weather_condition"]) +
        (priority_score_value * weights["priority"])
    )

    return total_score


def pilot_score(pilot:Pilot):
    return pilot.skill / 10

def general_weather_score(weather:Weather):
    weather_condition = weather_score(weather)
    cloud_state = weather.clouds
    wind_state = weather.wind / 12 #0 - 12
    return weather_condition * (1/3) + cloud_state *(1/3) + wind_state * (1/3)

def priority_score(target:Target):
    return target.priority / 5;

def distance_score(aircraft: Aircraft, distance):
    reltio = distance / aircraft.fuel_capacity
    return 1 if reltio > 1 else reltio

def weather_score (weather):
    if weather.condition == "Clear":
        return 1.0 # Best condition
    elif weather.condition == "Clouds":
        return 0.7 # clouds are moderate
    elif weather.condition == "Rain":
        return 0.4 # Rainy weather
    elif weather.condition == "Stormy":
        return 0.2 # Stormy weather is least favorable
    else:
        return 0 # Unfavorable condition

