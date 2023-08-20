import random

## Ground humidity sensor (YL69)
LOWER_BOUND = 0
UPPER_BOUND = 4095

def GetGroundHumiditySensor_decorator(f):
    def inner():
        return_value = f()
        print('GroundHumiditySensorValue is: ', return_value)
        return return_value
    return inner

@GetGroundHumiditySensor_decorator
def GetSensorReading() -> float:
    return random.randrange(LOWER_BOUND, UPPER_BOUND) # arduino due adc analogRead return range