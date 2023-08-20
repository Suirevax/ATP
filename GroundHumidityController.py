import GroundHumiditySensor
import GroundHumidityActuator
import HelperFunctions

def WaterConvertReadingToAction(value: float) -> float:
    return HelperFunctions.normalize(GroundHumidityActuator.LOWER_BOUND,GroundHumidityActuator.UPPER_BOUND, GroundHumiditySensor.LOWER_BOUND, GroundHumiditySensor.UPPER_BOUND, value) # actuator has range from 0 to 255

def Update() -> None:
    GroundHumidityActuator.SetWaterFlow(WaterConvertReadingToAction(GroundHumiditySensor.GetSensorReading()))
    return