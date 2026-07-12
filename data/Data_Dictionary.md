# Data Dictionary

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| Mission_ID | Text | Unique mission identifier |
| Mission_Date | Date | Date of the mission |
| Mission_Type | Text | Surveillance, Rescue, Delivery, Mapping, Inspection |
| Drone_Model | Text | Drone model used for the mission |
| Operator_ID | Text | Unique operator identifier |
| Base_Location | Text | Mission starting location |
| Flight_Duration_Min | Number | Total flight duration in minutes |
| Distance_Km | Decimal | Distance covered during the mission |
| Battery_Start | Number | Battery percentage before takeoff |
| Battery_End | Number | Battery percentage after landing |
| Battery_Consumed | Number | Battery_Start - Battery_End |
| Altitude_m | Number | Average flight altitude |
| Payload_Type | Text | Camera, Medical Kit, Sensor, Food Supplies, None |
| Payload_Weight_kg | Decimal | Payload weight in kilograms |
| Weather | Text | Clear, Cloudy, Rainy, Foggy, Windy |
| Wind_Speed_kmph | Number | Wind speed during flight |
| Temperature_C | Number | Temperature during mission |
| Threat_Level | Text | Low, Medium, High, Critical |
| Signal_Strength | Text | Excellent, Good, Fair, Poor |
| Mission_Status | Text | Success, Failed, Aborted |
| Failure_Reason | Text | Reason for failure (if applicable) |
| Mission_Score | Number | Overall mission performance score (0–100) |