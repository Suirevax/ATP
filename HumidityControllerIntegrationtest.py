import unittest
import GroundHumidityController
import GroundHumiditySensor
import GroundHumidityActuator

class TestSensorToActuatorConverstion(unittest.TestCase):
    def test_input_higher_than_ideal_constant(self):
        self.assertEqual( 
            GroundHumidityController.WaterConvertReadingToAction(GroundHumidityController.IDEAL_HUMIDITY_SENSOR_VOLTAGE + 1)
            , 0, 'Wrong return value when input is the higher as the ideal voltage')
    

    def test_input_same_as_ideal_constant(self):
        self.assertEqual(
            GroundHumidityController.WaterConvertReadingToAction(GroundHumidityController.IDEAL_HUMIDITY_SENSOR_VOLTAGE)
            , 0, 'Wrong return value when input is the same as the ideal voltage')
    
    def test_input_1_lower_as_ideal_constant(self):
        self.assertAlmostEqual(
            GroundHumidityController.WaterConvertReadingToAction(GroundHumidityController.IDEAL_HUMIDITY_SENSOR_VOLTAGE - 1)
            , 0, 0, 'Wrong return value when input is 1 lower than ideal voltage')
        
    def test_input_equals_lower_bound(self):
        self.assertAlmostEqual(
            GroundHumidityController.WaterConvertReadingToAction(GroundHumiditySensor.LOWER_BOUND)
            , 255, 0, 'Wrong return value when input is equal to sensor lower bound')
        
    def test_input_upper_bound(self):
        self.assertEqual(
            GroundHumidityController.WaterConvertReadingToAction(GroundHumiditySensor.UPPER_BOUND)
            , 0, 'Wrong return value when input is equal to sensor upper bound')
        
    def test_input_large_positive_int(self):
        self.assertEqual(
            GroundHumidityController.WaterConvertReadingToAction(2147483647)
            , 0, 'Wrong return value when input is large positive int')
    
    def test_input_large_negative_int(self):
        self.assertEqual(
            GroundHumidityController.WaterConvertReadingToAction(-2147483647)
            , None, 'Wrong return value when input is large negative int')
        
    def test_input_middle_value(self):
        self.assertEqual(
            GroundHumidityController.WaterConvertReadingToAction((GroundHumidityController.IDEAL_HUMIDITY_SENSOR_VOLTAGE + GroundHumiditySensor.LOWER_BOUND) / 2)
            , (GroundHumidityActuator.LOWER_BOUND + GroundHumidityActuator.UPPER_BOUND) / 2 , 'Wrong return value when input is middleValue')

if __name__ == '__main__':
    unittest.main()