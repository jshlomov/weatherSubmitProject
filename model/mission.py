
class Mission:
    def __init__(self, target_city, priority, assigned_pilot, assigned_aircraft,
                 distance, weather_condition, pilot_skill, aircraft_speed,
                 fuel_capacity, missin_fit_score):
        self.target_city = target_city
        self.priority = priority
        self.assigned_pilot = assigned_pilot
        self.assigned_aircraft = assigned_aircraft
        self.distance = distance
        self.weather_condition = weather_condition
        self.pilot_skill = pilot_skill
        self.aircraft_speed = aircraft_speed
        self.fuel_capacity = fuel_capacity
        self.missin_fit_score = missin_fit_score

    def __str__(self):
        return f"target_city: {self.target_city}, missin_fit_score: {self.missin_fit_score}"