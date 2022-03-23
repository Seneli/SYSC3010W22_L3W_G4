import unittest
import classes.device as Device

class Test_CovidRapidScreeener(unittest.TestCase):
    
    def test_create_device_default_values(self):
        device = Device()
        self.asserEqual(device.system_number, 1)
        self.asserEqual(device.owner, "L3W_G4")
        self.asserEqual(owner.contact_info, "L3W.G4.SAD@gmail.com")
        
        """
    def test_create_device(self):
        rapidS = yourObject()
        rapidS.createNewDevice(id=999999)
        id = rapidS.getId()
        self.assertEqual(id, 999999)
        owner = rapidS.getOwner(id=999999)
        self.asserEqual(owner, "TestOwner")
    
    def test_readFromDb(self):
        unittest.mock()
        """
    

if __name__ == '__main__':
    unittest.main(verbosity=2)