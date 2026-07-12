"""
config.py
Configuration file for Aerial Shield Dataset Generator
"""

TOTAL_RECORDS = 5000

MISSION_TYPES = [
    "Surveillance",
    "Reconnaissance",
    "Search & Rescue",
    "Medical Delivery",
    "Infrastructure Inspection",
    "Border Patrol"
]

DRONE_MODELS = [
    "DJI Matrice 300 RTK",
    "DJI Mavic 3 Enterprise",
    "Autel EVO Max 4T",
    "Parrot Anafi AI",
    "Skydio X2D"
]

BASE_LOCATIONS = [
    "Delhi",
    "Jaipur",
    "Chandigarh",
    "Lucknow",
    "Shimla",
    "Dehradun"
]

PAYLOAD_TYPES = [
    "HD Camera",
    "Thermal Camera",
    "Medical Kit",
    "Food Package",
    "LiDAR",
    "Sensor Package"
]

OPERATORS = [
    f"OP-{i:03d}" for i in range(1,31)
]