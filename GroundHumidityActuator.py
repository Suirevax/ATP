## watertap actuator, 180 degrees servo motor (MG996R)
LOWER_BOUND = 0
UPPER_BOUND = 255

def SetWaterFlow(value: int) -> None:
    print("Set MG996R value to: " + str(value))
    return