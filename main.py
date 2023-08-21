import time
import LightIntensityController
import GroundHumidityController

def main():
    while(True):
        print("Update")
        GroundHumidityController.Update()
        LightIntensityController.Update()
        time.sleep(1)

if __name__ == "__main__":
    if(False): # Add Decorator
        import GroundHumiditySensor
        def GetGroundHumiditySensor_decorator(f):
            def inner():
                return_value = f()
                print('GroundHumiditySensorValue is:', return_value)
                return return_value
            return inner

        GroundHumiditySensor.GetSensorReading = GetGroundHumiditySensor_decorator(GroundHumiditySensor.GetSensorReading)
        del GroundHumiditySensor
    
    if(True): # systemtest
        print("Prepare systemtest")
        import random
        
        import GroundHumiditySensor
        def SystemTest_GroundHumidity_SensorReading():
            return_value = random.randrange(GroundHumiditySensor.LOWER_BOUND, GroundHumiditySensor.UPPER_BOUND)
            print("GetHumiditySensor Return value:", return_value)
            return return_value
        GroundHumiditySensor.GetSensorReading = SystemTest_GroundHumidity_SensorReading

        import LightIntensitySensor
        def SystemTest_LightIntensity_SensorReading():
            return_value = random.randint(LightIntensitySensor.LOWER_BOUND, LightIntensitySensor.UPPER_BOUND)
            print("GetLightSensor Return value:", return_value)
            return return_value
        LightIntensitySensor.GetSensorReading = SystemTest_LightIntensity_SensorReading

        import GroundHumidityActuator
        def SystemTest_GroundHumidity_Actuator(a):
            print("GroundHumidityActuatorAction:", a)
        GroundHumidityActuator.SetWaterFlow = SystemTest_GroundHumidity_Actuator

        import LightIntensityActuator
        def SystemTest_LightIntensity_Actuator(a):
            print("LightIntensityActuatorAction:", a)
        LightIntensityActuator.SetResistance = SystemTest_LightIntensity_Actuator

    main()