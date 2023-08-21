import random

## Ground humidity sensor (YL69)
LOWER_BOUND = 0
UPPER_BOUND = 4095

def dummy_analogue_read():
    return LOWER_BOUND

analog_read = dummy_analogue_read

def GetSensorReading() -> float:
    return analog_read() # arduino due adc analogRead return range