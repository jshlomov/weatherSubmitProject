from model.Location import Location


def extract_location_from_json(json):
    return Location(json[0]["lat"], json[0]["lon"])