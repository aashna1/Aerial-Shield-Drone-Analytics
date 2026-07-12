import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

random.seed(42)

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

WEATHER = [
    "Clear",
    "Cloudy",
    "Rainy",
    "Foggy",
    "Windy"
]

PAYLOADS = [
    "HD Camera",
    "Thermal Camera",
    "Medical Kit",
    "Food Package",
    "LiDAR",
    "Sensor Package"
]

BASES = [
    "Delhi",
    "Jaipur",
    "Lucknow",
    "Chandigarh",
    "Dehradun",
    "Shimla"
]

MISSIONS = []

start_date = datetime(2025,1,1)

for i in range(1,5001):

    duration = random.randint(20,90)

    distance = round(random.uniform(5,60),2)

    altitude = random.randint(80,300)

    battery_start = 100

    battery_consumed = random.randint(20,85)

    battery_end = battery_start-battery_consumed

    weather = random.choice(WEATHER)

    temperature = random.randint(8,42)

    wind = random.randint(3,35)

    payload = random.choice(PAYLOADS)

    payload_weight = round(random.uniform(0.5,5),2)

    threat = random.choice(["Low","Medium","High","Critical"])

    operator = f"OP-{random.randint(1,30):03d}"

    mission_date = start_date + timedelta(days=random.randint(0,364))

    success_probability = 0.95

    if weather=="Rainy":
        success_probability -=0.15

    if battery_end<20:
        success_probability -=0.20

    if threat=="Critical":
        success_probability -=0.10

    status="Success"

    failure_reason="NA"

    if random.random()>success_probability:

        status="Failed"

        failure_reason=random.choice([
            "Battery Failure",
            "Weather",
            "Signal Loss",
            "Mechanical Fault"
        ])

    mission_score=max(
        50,
        min(
            100,
            int(
                100
                -(100-success_probability*100)
                +random.randint(-5,5)
            )
        )
    )

    MISSIONS.append({

        "Mission_ID":f"ASD-{i:05d}",

        "Mission_Date":mission_date.strftime("%Y-%m-%d"),

        "Mission_Type":random.choice(MISSION_TYPES),

        "Drone_Model":random.choice(DRONE_MODELS),

        "Base_Location":random.choice(BASES),

        "Operator_ID":operator,

        "Flight_Duration_Min":duration,

        "Distance_Km":distance,

        "Altitude_m":altitude,

        "Battery_Start":battery_start,

        "Battery_End":battery_end,

        "Battery_Consumed":battery_consumed,

        "Payload_Type":payload,

        "Payload_Weight_kg":payload_weight,

        "Weather":weather,

        "Temperature_C":temperature,

        "Wind_Speed_kmph":wind,

        "Threat_Level":threat,

        "Mission_Status":status,

        "Failure_Reason":failure_reason,

        "Mission_Score":mission_score

    })

df=pd.DataFrame(MISSIONS)

df.to_csv("output/Aerial_Shield_Drone_Data.csv",index=False)

df.to_excel("output/Aerial_Shield_Drone_Data.xlsx",index=False)

print(df.head())

print(df.shape)

print("\nDataset Generated Successfully.")