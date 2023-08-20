import time
import LightIntensityController
import GroundHumidityController

if(True): # Add Decorator
    import GroundHumiditySensor
    def GetGroundHumiditySensor_decorator(f):
        def inner():
            return_value = f()
            print('GroundHumiditySensorValue is:', return_value)
            return return_value
        return inner

    GroundHumiditySensor.GetSensorReading = GetGroundHumiditySensor_decorator(GroundHumiditySensor.GetSensorReading)
    del GroundHumiditySensor

def main():
    while(True):
        print("Update")
        GroundHumidityController.Update()
        LightIntensityController.Update()
        time.sleep(1)

if __name__ == "__main__":
    main()