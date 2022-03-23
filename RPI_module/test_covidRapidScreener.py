import unittest

class Test_CovidRapidScreeener(unittest.TestCase):
    def test_create_device(self):
        rapidS = yourObject()
        rapidS.createNewDevice(id=999999)
        id = rapidS.getId()
        self.assertEqual(id, 999999)
        owner = rapidS.getOwner(id=999999)
        self.asserEqual(owner, "TestOwner")
    
    def test_readFromDb(self):
        unittest.mock()
    

