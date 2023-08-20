import random

## Ground humidity sensor (YL69)
LOWER_BOUND = 0
UPPER_BOUND = 4095



def GetSensorReading() -> float:
    return random.randrange(LOWER_BOUND, UPPER_BOUND) # arduino due adc analogRead return range