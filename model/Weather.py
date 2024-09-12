class Weather:

    def __init__(self, condition, clouds, wind, date):
        self.condition = condition
        self.clouds = clouds
        self.wind = wind
        self.date = date

    def __str__(self):
        return f"condition: {self.condition}, clouds: {self.clouds}, wind: {self.wind}, date: {self.date}"