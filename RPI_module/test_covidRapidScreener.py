import unittest
import firebase_admin
from datetime import datetime
import os
from classes.device import Device

class Test_CovidRapidScreener(unittest.TestCase):
    
    def setUp(self):
        self.device = Device()
    
    def tearDown(self):
        self.device.die()
    
    
    def test_create_device_default_values(self):
        self.assertEqual(self.device.system_number, 1)
        self.assertEqual(self.device.owner, "L3W_G4")
        self.assertEqual(self.device.contact_info, "L3W.G4.SAD@gmail.com")
    
    """
    def test_create_device_custom_values(self):
        device = Device(5, "test_owner", "test_contact")
        self.assertEqual(device.system_number, 5)
        self.assertEqual(device.owner, "test_owner")
        self.assertEqual(device.contact_info, "test_contact")
    """
    
    def test_initialize_rtdb_datastruct(self):
        expected_result = {
            "Failed_Screenings": {
                "DATE": {
                "STUDENT NUMBER": {
                        "ReasonForFailure": 1
                    }
                }
            },
            "System_Variables": {
                "currentUser": "",
                "passedMaskDetection": "null",
                "passedTempDetection": "null",
                "runDetection": "false"
            }
        }
        var = self.device.firebase.get_this_devices_datastruct()
        self.assertEqual(var, expected_result)
        
    def test_get_system_variables(self):
        expected_result = {
            "currentUser": "",
            "passedMaskDetection": "null",
            "passedTempDetection": "null",
            "runDetection": "false"
        }
        sys_var = self.device.firebase.get_System_Variables()
        self.assertEqual(sys_var, expected_result)
        
    def test_get_passedMaskDetection(self):
        expected_result = "null"
        result = self.device.firebase.get_passedMaskDetection()
        self.assertEqual(result, expected_result)
        
    def test_get_runDetection(self):
        expected_result = "false"
        result = self.device.firebase.get_runDetection()
        self.assertEqual(result, expected_result)   
      
    def test_take_picture(self):
        os.remove("images/test.jpg")
        self.assertFalse(os.path.exists("images/test.jpg"))
        self.device.camera.capture_image("./images/", "test.jpg")
        self.assertTrue(os.path.exists("images/test.jpg"))
    
    
    def test_put_image_in_storage(self):
        date_time = datetime.today().strftime("%m%d%Y%H%M%S")
        print(date_time + ".jpg")
        self.device.firebase.put_image_in_storage(date_time+".jpg", "test.jpg")
        #self.assertTrue(True) #check it exists on there? 
    
    

if __name__ == '__main__':
    unittest.main(verbosity=2)