from firebase_admin import credentials, initialize_app, db, storage
from datetime import datetime

class FireBase:

    def __init__(self, system_number = 1):

        cred = credentials.Certificate("firebase-sdk.json")
        initialize_app(cred, {
            'databaseURL': 'https://covid-rapid-screener-default-rtdb.firebaseio.com/',
            'storageBucket': 'covid-rapid-screener.appspot.com'
        })
        self.init = True
        self.system_number = system_number
        self.storage = storage.bucket()

        # Put your local file path 
    def put_image_in_storage(self, image_name_on_storage, image_name_on_local):
        blob = self.storage.blob("images/" + image_name_on_storage)
        blob.upload_from_filename("./images/" + image_name_on_local)

    #initialize data structure in DATABASE
    def initialize_rtdb_datastruct(self):
        baseRef = db.reference('/')
        baseRef.child(self.system_number).set({
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
        })

    def get_System_Variables(self):
        print("Getting System_Variables")
        ref = db.reference(self.system_number + "/System_Variables")
        return ref.get()
    
    def get_passedMaskDetection(self):
        print("Getting runDetection")
        ref = db.reference(self.system_number + "/System_Variables/passedMaskDetection")
        return ref.get()
    
    def get_runDetection(self):
        print("Getting runDetection")
        ref = db.reference(self.system_number + "/System_Variables/runDetection")
        return ref.get()
    
    def update_currentUser(self, name):
        ref = db.reference(self.system_number + "/System_Variables")
        ref.update({
            'currentUser' : name,
            'runDetection' : 'true'
        })

    def log_failed_user(self, date, current_user, reason_for_failure) :
        print("logging failed user")
        ref = db.reference(self.system_number + "/Failed_Screenings")
        ref.child(date).set({
                current_user : {
                    "reasonForFailure" : reason_for_failure
                }
        })