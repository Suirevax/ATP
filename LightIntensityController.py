import LightIntensitySensor
import LightIntensityActuator
import HelperFunctions

def LightConvertReadingToAction(value: int) -> int:
    return HelperFunctions.normalize(LightIntensityActuator.LOWER_BOUND, LightIntensityActuator.UPPER_BOUND, LightIntensitySensor.LOWER_BOUND, LightIntensitySensor.UPPER_BOUND, value) # actuator has range from 0 to 255

def Update() -> None:
    LightIntensityActuator.SetResistance(LightConvertReadingToAction(LightIntensitySensor.GetSensorReading()))
    return