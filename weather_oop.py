import requests
import json


class WeatherToday:
    def __init__(self, latitude: float, longitude: float):
        self.__location_latitude = latitude
        self.__location_longitude = longitude
        self.__WEATHER_APP_ID = "9ca00eded167e18c468b2beda2ec4d1b"
        self.__WEATHER_APP_URL = "https://api.openweathermap.org/data/2.5/weather"
        
    def __prepare_params(self) -> dict:
        """
        Prepares the parameters to be used to make request
        Important parameters:lon, kat appId
        NB: Must be invoked when we want to make a weather request
        """
        params = {
            "lat": self.__location_latitude,
            "lon": self.__location_longitude,
            "appId": self.__WEATHER_APP_ID
        }
        return params
    def get_location_longitude(self):
        return self.__location_longitude
    
    def set_location_longitude(self, modified_longitude):
        self.__location_longitude = modified_longitude
        
    def get_location_latitude(self):
        return self.__location_latitude
    
    def set_location_latitude(self, modified_latitude):
        self.__location_latitude = modified_latitude
        
    def __get_weather_raw(self) -> dict:
        weather_params = self.__prepare_params()
        weather_results  = requests.get(self.__WEATHER_APP_URL, weather_params)
        # return json.dumps(weather_results.json(), indent=4)
        return weather_results.json()
    
    def get_weather(self) -> str:
        weather_raw = self.__get_weather_raw()
        result_latitude = weather_raw["coord"]["lat"]
        result_longitude = weather_raw["coord"]["lon"]
        result_weather = weather_raw["weather"][0]["description"]
        result_temperature = weather_raw['main']["temp"] -273
        formated_temperature = "{:.2f}".format(result_temperature)
        result_city = weather_raw["name"]
        result = f"LATITUDE: {result_latitude}\nLONGITUDE: {result_longitude}\nCITY: {result_city}\nWEATHER: {result_weather}\nTEMPERATURE: {formated_temperature} degrees"

        return result
        
    
        
    
weather_today = WeatherToday( -1.1079495110608915, 37.01376809257765)
# print(weather_today.get_weather())
# print(weather_today.__WEATHER_APP_ID)
# print(weather_today.__prepare_params())
# weather_today.__location_longitude = 59302
# print(weather_today.__location_longitude)
# print(weather_today.get_location_longitude())
# weather_today.set_location_longitude(59302)
# print(weather_today.get_location_longitude())
weather_today.__location_latitude = 59302
print(weather_today.__location_latitude)
print(weather_today.get_location_latitude())
weather_today.set_location_latitude(59302)
print(weather_today.get_location_latitude())
