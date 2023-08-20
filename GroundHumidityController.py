import GroundHumiditySensor
import GroundHumidityActuator
import HelperFunctions

IDEAL_HUMIDITY_SENSOR_VOLTAGE = 3000

def WaterConvertReadingToAction(value: float) -> float:
    if (value >= IDEAL_HUMIDITY_SENSOR_VOLTAGE):
        return 0
    flipped_sensor_value = IDEAL_HUMIDITY_SENSOR_VOLTAGE - (value - GroundHumiditySensor.LOWER_BOUND)
    return HelperFunctions.normalize(GroundHumidityActuator.LOWER_BOUND,GroundHumidityActuator.UPPER_BOUND, GroundHumiditySensor.LOWER_BOUND, IDEAL_HUMIDITY_SENSOR_VOLTAGE, flipped_sensor_value)

def Update() -> None:
    GroundHumidityActuator.SetWaterFlow(WaterConvertReadingToAction(GroundHumiditySensor.GetSensorReading()))
    return