import requests
import json

weather_url = "https://api.openweathermap.org/data/2.5/weather"
weather_parameters = {
    "lat": -1.1079495110608915,
    "lon": 37.01376809257765,
    "appId": "9ca00eded167e18c468b2beda2ec4d1b"
}
weather_response = requests.get(weather_url, weather_parameters)
parsed_data = (weather_response.json())
print(json.dumps(parsed_data, indent=4))

# print(weather_response.json)