from model.Weather import Weather


def extract_weather_from_json(json):
    condition = json["list"][0]["weather"][0]["main"]
    clouds = json["list"][0]["clouds"]["all"]
    wind = json["list"][0]["wind"]["speed"]
    date = json["list"][0]["dt_txt"]
    return Weather(condition, clouds, wind, date)