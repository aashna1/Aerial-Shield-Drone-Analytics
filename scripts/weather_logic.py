"""
weather_logic.py
"""

import random

WEATHER = [
    "Clear",
    "Cloudy",
    "Rainy",
    "Foggy",
    "Windy"
]

def generate_weather():

    weather = random.choices(

        WEATHER,

        weights=[45,20,15,10,10],

        k=1

    )[0]

    if weather == "Clear":
        wind = random.randint(5,15)

    elif weather == "Cloudy":
        wind = random.randint(8,18)

    elif weather == "Rainy":
        wind = random.randint(10,28)

    elif weather == "Foggy":
        wind = random.randint(3,10)

    else:
        wind = random.randint(20,40)

    return weather, wind