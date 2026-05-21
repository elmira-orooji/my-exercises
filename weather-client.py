# modules and global variables
from abc import ABC, abstractmethod
import requests


# abstract class
class WeatherAbstract(ABC):

    @abstractmethod
    def get_current_weather(self, lat, lon):
        pass



# openwather class
class OpenWeatherProvider(WeatherAbstract):
    base_url = "https://api.openweathermap.org/data/2.5/wather"
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, lat, lon):
        params = {
            "lat":lat,
            "lon":lon,
            "appid":self.api_key
        }
        response = requests.get(self.base_url,params=params)
        normalized_data = {"temp":float(response.json()["main"]["temp"]) - 273.15, "humidity":response.json()["main"]["humidity"]}
        return normalized_data

# openmeteo class
class OpenMeteoProvider(WeatherAbstract):
    base_url = 'https://api.open-meteo.com/v1/forecast'
    def get_current_weather(self, lat, lon):
        params = {
            "latitude":lat,
            "longitude":lon,
            "current":"temperature_2m,relative_humidity_2m"
        }
        response = requests.get(self.base_url, params=params)
        normalized_data = {"temp":response.json()["current"]["temperatue_2m"], "humidity":response.json()["current"]["relative_humidity_2m"]}
        return normalized_data


# running the application
provider = OpenMeteoProvider()
print(provider.get_current_weather(lat=35.82472320684597, lon=51.00105750513447))