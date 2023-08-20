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
    main()