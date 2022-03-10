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

def init():
    db.child("System_variables").child("runDetection").set("false")
    db.child("System_variables").child("passedMaskDetection").set("null")
    db.child("System_variables").child("passedTempDetection").set("null")
    db.child("System_variables").child("currentUser").set("null")
    
def fetchList():
    #create a list of that days studentIDs
    date = datetime.today().strftime('%Y-%m-%d')
    date_data = db.child(date).get()
    date_list = date_data.each()
    
    #create a list of the system variables
    sys_data = db.child("System_variables").get()
    sys_list = sys_data.each()
    
    return [date_list, date_data, sys_list, sys_data]

def runDetection():
    
    #create a list of
    print("Running detection")
    while(True):
        date = datetime.today().strftime('%Y-%m-%d')
        data = fetchList()
        print(data[2][0].val())
        # if runDetection is true
        if (data[2][3].val() == "true"):
            # take a picture
            print("PiCam takes picture")
            time.sleep(1)
            # test the picture for mask
            print("test picture for mask")
            time.sleep(1)
            # get result of test
            # save value in passedMaskDetection
            print("check temperature")
            time.sleep(1)
            # check for highest temperature
            # save value in passedTempDetection
            print("save values to firebase")
            time.sleep(1)
            
            # save student ID
            ID = data[2][0].val()
            
            print("check for which test passed and/or failed")
            time.sleep(1)
            print("both tests failed")
            time.sleep(1)
            #if mask detection failed and temp detection failed
            if((data[2][1].val()) == "false" and (data[2][2].val() == "false")):
                #save the saved picture
                db.child(date).child(ID).child("MaskDetected").set("false")
                db.child(date).child(ID).child("TempDetected").set("false")
                db.child("System_variables").child("passedMaskDetection").set("false")
                db.child("System_variables").child("passedTempDetection").set("false")
                storage.child("image.jpg").put("image.jpg")
        
            #if mask detection failed and temp detection successful
            elif((data[2][1].val() == "false") and (data[2][2].val() == "true")):
                print("only mask detection failed")
                time.sleep(1) 
                #save the saved picture
                db.child(date).child(ID).child("MaskDetected").set("false")
                db.child(date).child(ID).child("TempDetected").set("true")
                db.child("System_variables").child("passedMaskDetection").set("false")
                db.child("System_variables").child("passedTempDetection").set("true")
                storage.child("image.jpg").put("image.jpg")
            
            #if mask detection successful and temp detection failed
            elif((data[2][1].val()) == "true" and (data[2][2].val() == "false")):
                print("only temp detection failed")
                time.sleep(1)
                #save the saved picture
                db.child(date).child(ID).child("MaskDetected").set("true")
                db.child(date).child(ID).child("TempDetected").set("false")
                db.child("System_variables").child("passedMaskDetection").set("true")
                db.child("System_variables").child("passedTempDetection").set("false")
                storage.child("image.jpg").put("image.jpg")

            #if mask detection was successful
            else:                 
                print("both tests passed")
                time.sleep(1)
                db.child(date).child(ID).child("MaskDetected").set("true")
                db.child(date).child(ID).child("TempDetected").set("true")
                db.child("System_variables").child("passedMaskDetection").set("true")
                db.child("System_variables").child("passedTempDetection").set("true")
                #delete the saved picture

        # if we want to run a test
        elif(data[2][3].val() == "test"):   
            print("running test")
            time.sleep(1)
            ID = data[2][0].val()
            #save the saved picture
            db.child(date).child("test").child("MaskDetected").set("test")
            db.child(date).child("test").child("TempDetected").set("test")
            db.child("System_variables").child("passedMaskDetection").set("test")
            db.child("System_variables").child("passedTempDetection").set("test")
            storage.child("image.jpg").put("image.jpg")
        time.sleep(1)
        

init()
db.child("System_variables").child("runDetection").set("test")
runDetection()


