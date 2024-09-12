# Reads data from a JSON file
import json

from toolz import curry

from model.Aircraft import Aircraft
from model.Pilot import Pilot
from model.Target import Target


def read_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

@curry
def write_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# def append_to_file(filename, data):
#     with open(filename, 'a') as f:
#         f.write(data)

def convert_target_from_json(json):
    return

def read_aircraft_from_json(filename):
    with open(filename, 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Aircraft(**aircraft) for aircraft in data["aircrafts"]]


def read_pilot_from_json(filename):
    with open(filename, 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Pilot(**pilot) for pilot in data["pilots"]]

def read_target_from_json(filename):
    with open(filename, 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Target(**target) for target in data["targets"]]