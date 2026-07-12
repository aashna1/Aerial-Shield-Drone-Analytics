"""
Aerial Shield
Drone Mission Dataset Generator

Author: Aashna Kashyap
"""

import random
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

random.seed(42)
np.random.seed(42)

TOTAL_RECORDS = 5000

MISSION_TYPES = [
    "Surveillance",
    "Rescue",
    "Delivery",
    "Mapping",
    "Inspection"
]

DRONE_MODELS = [
    "DJI Matrice 300 RTK",
    "Skydio X2",
    "Parrot Anafi AI",
    "Autel EVO Max 4T",
    "DJI Mavic 3 Enterprise"
]

WEATHER = [
    "Clear",
    "Cloudy",
    "Rainy",
    "Foggy",
    "Windy"
]

THREAT_LEVEL = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

PAYLOAD = [
    "Camera",
    "Medical Kit",
    "Sensor",
    "Food Supplies",
    "None"
]

print("Configuration Loaded Successfully!")