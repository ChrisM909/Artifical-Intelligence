# Programmer: Christopher Melbow
# Date: 2.29.2024
# Program: AI Playground

print("This wil be a place to play with programming using AI Technology\n")
import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]

        print(f"Weather in {city}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        print(f"Error: Unable to fetch weather information. Status code: {response.status_code}")


# Replace 'YOUR_API_KEY' with the API key you obtained from OpenWeatherMap
api_key = 'ada71058b408099a065a3683bfb5b363'
city_name = 'Richland'

get_weather(api_key, city_name)