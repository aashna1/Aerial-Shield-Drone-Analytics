"""
battery_logic.py
"""

import random

def battery_usage(duration):

    consumption = int(duration*0.85 + random.randint(5,18))

    consumption = min(consumption,95)

    end = 100-consumption

    return 100,end,consumption