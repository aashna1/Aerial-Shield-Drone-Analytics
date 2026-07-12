"""
mission_generator.py

Generates a realistic drone mission.
"""

import random
from datetime import datetime, timedelta

from config import (
    MISSION_TYPES,
    DRONE_MODELS,
    BASE_LOCATIONS,
    PAYLOAD_TYPES,
    OPERATORS
)

from weather_logic import generate_weather
from battery_logic import battery_usage


def generate_mission(mission_id):

    date = datetime(2025, 1, 1) + timedelta(
        days=random.randint(0, 364)
    )

    mission_type = random.choice(MISSION_TYPES)

    drone = random.choice(DRONE_MODELS)

    operator = random.choice(OPERATORS)

    location = random.choice(BASE_LOCATIONS)

    duration = random.randint(18, 95)

    distance = round(random.uniform(4, 55), 2)

    altitude = random.randint(70, 300)

    payload = random.choice(PAYLOAD_TYPES)

    payload_weight = round(random.uniform(0.5, 5.0), 2)

    weather, wind = generate_weather()

    battery_start, battery_end, battery_consumed = battery_usage(duration)

    mission = {

        "Mission_ID": f"ASD-{mission_id:05d}",

        "Mission_Date": date.strftime("%Y-%m-%d"),

        "Mission_Type": mission_type,

        "Drone_Model": drone,

        "Operator_ID": operator,

        "Base_Location": location,

        "Flight_Duration_Min": duration,

        "Distance_Km": distance,

        "Battery_Start": battery_start,

        "Battery_End": battery_end,

        "Battery_Consumed": battery_consumed,

        "Altitude_m": altitude,

        "Payload_Type": payload,

        "Payload_Weight_kg": payload_weight,

        "Weather": weather,

        "Wind_Speed_kmph": wind

    }

    return mission