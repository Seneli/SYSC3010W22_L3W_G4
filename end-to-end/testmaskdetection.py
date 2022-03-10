import pyrebase
import time
from datetime import datetime
# for end to end demo purposes

# Create new Firebase config and database object
config = {
  "apiKey": "AIzaSyCQwrsJrmcvLNvCxikx3m3f04oQeJk_x-s",
  "authDomain": "covid-rapid-screener.firebaseapp.com",
  "databaseURL": "https://covid-rapid-screener-default-rtdb.firebaseio.com/",
  "storageBucket": "covid-rapid-screener.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

def download_image(image_name):
    storage.child(image_name).download(filename="ml1.jpg", path='/Users/senster/Projects/SYSC3010/SYSC3010Project/end-to-end/')
    #storage.delete(image_name)

def set_mask_detection_result(result):
    db.child("System_variables").child("passedMaskDetection").set(result)


download_image("image.jpg")
set_mask_detection_result(True)
time.sleep(10)
set_mask_detection_result(False)