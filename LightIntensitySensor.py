import random

## Light intensity sensor (BH1750)
LOWER_BOUND = 1  # sensor has range from 1 to 65535
UPPER_BOUND = 65535

def GetSensorReading() -> int:
        return random.randint(LOWER_BOUND, UPPER_BOUND)