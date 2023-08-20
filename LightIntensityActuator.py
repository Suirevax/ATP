## Sunlamp intensity actuator/ resistor (AD5206)
LOWER_BOUND = 0
UPPER_BOUND = 255

def SetResistance(value: int) -> None:
    print("Set AD5206 Resistance to: " + str(value))
    return