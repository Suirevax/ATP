import ctypes
import pathlib

## watertap actuator, 180 degrees servo motor (MG996R)
LOWER_BOUND = 0
UPPER_BOUND = 255

# ctypes_test.py
import ctypes
import pathlib

PIN_NUMBER = 2

libname = pathlib.Path().absolute() / "arduino.so"
libObject = ctypes.CDLL(libname)

def SetWaterFlow(value: int) -> None:
    ## Pretend this controls the pwm
    libObject.analogWrite(PIN_NUMBER,int(value))
    return