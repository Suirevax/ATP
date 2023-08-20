import unittest
import HelperFunctions

class TestSensorToActuatorConverstion(unittest.TestCase):
    def test_normal_1(self):
        self.assertEqual(HelperFunctions.normalize(0,100,0,10,5),50)
        
    def test_normal_2(self):
        self.assertEqual(HelperFunctions.normalize(20,120,0,10,8),100)

    def test_normal_2(self):
        self.assertEqual(HelperFunctions.normalize(50,300,0,10,8),250)
    
    def test_input_equals_lower_source(self):
        self.assertEqual(HelperFunctions.normalize(87,100,0,10,0),87)
    
    def test_input_equals_upper_source(self):
        self.assertEqual(HelperFunctions.normalize(0,657,0,10,10),657)
    
    def test_destination_lower_bound_higher_than_destination_upper(self):
        self.assertEqual(HelperFunctions.normalize(105,100,0,10,5),None)
    
    def test_destination_lower_bound_higher_than_destination_upper_2(self):
        self.assertEqual(HelperFunctions.normalize(0,-100,0,10,5),None)
        
    def test_source_lower_bound_higher_than_source_upper(self):
        self.assertEqual(HelperFunctions.normalize(0,100,15,10,5),None)
    
    def test_source_lower_bound_higher_than_source_upper(self):
        self.assertEqual(HelperFunctions.normalize(0,100,0,-10,5),None)
    
    def test_input_lower_than_lower_bound(self):
        self.assertEqual(HelperFunctions.normalize(0,100,0,10,-5),None)
    
    def test_input_higher_than_upper_bound(self):
        self.assertEqual(HelperFunctions.normalize(0,100,0,10,15),None)
        
if __name__ == '__main__':
    unittest.main()