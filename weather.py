import requests
import json


def weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2)
    temperature = str(round(weather_data['main']['temp']))
    temperature_feels = str(round(weather_data['main']['feels_like']))
    pressure = str(round(weather_data['main']['pressure']))
    humidity = str(round(weather_data['main']['humidity']))
    wind_speed = str(round(weather_data['wind']['speed']))
    return f'''
    Температура {temperature}°C
    Ощущается как {temperature_feels}°C
    Давление {pressure}Па
    Влажность {humidity}%
    Скорость ветра {wind_speed}м/с
    '''




