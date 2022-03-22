#import pyrebase
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

import camera

# global variables
system_number = "001"


#initialize connection to Firebase RealTimeDatabase
def connect_to_rtdb():
    cred = credentials.Certificate("private_lol/firebase-sdk.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://covid-rapid-screener-default-rtdb.firebaseio.com/'
    })

#initialize data structure in DATABASE
def initialize_rtdb_datastruct():
    baseRef = db.reference('/')
    baseRef.set({ 
        "001": {
            "Failed_Screenings": {
                "DATE": {
                "STUDENT NUMBER": {
                        "ReasonForFailure": 1
                    }
                }
            },
            "System_Variables": {
                "currentUser": 5,
                "passedMaskDetection": 5,
                "passedTempDetection": 5,
                "runDetection": 5
            }
        }
    })

def update_currentUser(name):
    ref = db.reference(system_number + "/System_Variables")
    ref.update({
        'currentUser' : name,
        'runDetection' : 'true'
    })

def get_runDetection():
    print("Getting runDetection")
    ref = db.reference(system_number + "/System_Variables/runDetection")
    return ref.get()

def get_passedMaskDetection():
    print("Getting runDetection")
    ref = db.reference(system_number + "/System_Variables/passedMaskDetection")
    return ref.get()

def get_System_Variables():
    print("Getting System_Variables")
    ref = db.reference(system_number + "/System_Variables")
    return ref.get()

def user_failed_screening(system_variables):
    print("put their name in the failed list")
    date = datetime.today().strftime('%Y-%m-%d')
    print("Getting System_Variables")
    ref = db.reference(system_number + "/Failed_Screenings")
    ref.push({
        
    })

def main():
    print("Creating connection to Firebase RealTime Database...")
    connect_to_rtdb()
    initialize_rtdb_datastruct()
    update_currentUser("monka")
    camera = get_camera()

    while(True):

        sys_var = get_System_Variables()
        if sys_var['runDetection'] == "true":
            
            #run mask detection stuff
            for i in range(10):
                print("PiCam takes picture")
                capture_image(camera, "/images")
                #insert image upload code here
                print("upload it to storage")

                passedMaskDetection = get_passedMaskDetection()
                if passedMaskDetection == "true":
                    #break for loop
                    continue 
                elif passedMaskDetection == "false":
                    user_failed_screening(sys_var)
                else:
                    #keep going in the loop
            
            #every loop check if it failed
            while(True):
                passedMaskDetection = get_passedMaskDetection()
                if passedMaskDetection == "true":
                    break
                elif passedMaskDetection == "false":
                    user_failed_screening(sys_var)
                    break

        if True:
            print("run temperature sensing stuff")
            print("check if it failed")

        #once it passes - delete all pictures in storage

 
        


if __name__ == "__main__":
    print("RPI Module starting...")
    main()
