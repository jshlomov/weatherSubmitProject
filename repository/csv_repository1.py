import csv
from typing import List
from toolz import  pipe, partial

from model.mission import Mission


def write_missions_to_csv(missions: List[Mission], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=[
        "target_city",
        "priority",
        "assigned_pilot",
        "assigned_aircraft",
        "distance",
        "weather_condition",
        "pilot_skill",
        "aircraft_speed",
        "fuel_capacity",
        "mission_fit_score"
    ])
            csv_writer.writeheader()

            for mission in missions:
                csv_writer.writerow({
                    'target_city': mission.target_city,
                    'priority': mission.priority,
                    'assigned_pilot': mission.assigned_pilot,
                    'assigned_aircraft': mission.assigned_aircraft,
                    'distance': mission.distance,
                    'weather_condition': mission.weather_condition,
                    'pilot_skill': mission.pilot_skill,
                    'aircraft_speed': mission.aircraft_speed,
                    'fuel_capacity': mission.fuel_capacity,
                    'mission_fit_score': mission.missin_fit_score
                })
    except Exception as e:
        print(e)