import ctypes
import pathlib

## watertap actuator, 180 degrees servo motor (MG996R)
LOWER_BOUND = 0
UPPER_BOUND = 255

# ctypes_test.py
import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    # libname = pathlib.Path().absolute() / "arduino.so"
    # c_lib = ctypes.CDLL(libname)

# libname = "c:\\Users\\rxpja\\Documents\\ATP\\automatische-plantenkas\\arduino.so"
# ctypes.cdll.LoadLibrary("arduino.so")
    libObject = ctypes.CDLL('arduino.so')

def SetWaterFlow(value: int) -> None:
    ## Pretend this controls the pwm
    arduino_lib.pwm_write(value)
    return