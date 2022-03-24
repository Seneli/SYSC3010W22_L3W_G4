from firebase_admin import credentials, initialize_app, db, storage, get_app, delete_app
from datetime import datetime

class FireBase:

    def __init__(self, system_number = 1, name="app"):
  
        self.name = name
        cred = credentials.Certificate("firebase-sdk.json")
        initialize_app(cred, {
            'databaseURL': 'https://covid-rapid-screener-default-rtdb.firebaseio.com/',
            'storageBucket': 'covid-rapid-screener.appspot.com'
        })
        self.app = get_app()
        self.system_number = str(system_number)
        self.storage = storage.bucket()
    
    def die(self):
        delete_app(self.app)

        # Put your local file path 
    def put_image_in_storage(self, image_name_on_storage, image_name_on_local):
        blob = self.storage.blob("images/" + image_name_on_storage)
        blob.upload_from_filename("./images/" + image_name_on_local)
        
    def check_image_exists_in_storage(self, image_name_in_storage):
        pass

    #initialize data structure in DATABASE
    def initialize_rtdb_datastruct(self):
        baseRef = db.reference('/', self.app)
        baseRef.child(self.system_number).set({
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
        })
    
    def get_this_devices_datastruct(self):
        baseRef = db.reference('/', self.app)
        return baseRef.child(self.system_number).get()

    def get_System_Variables(self):
        ref = db.reference(self.system_number + "/System_Variables", self.app)
        return ref.get()
    
    def get_passedMaskDetection(self):
        ref = db.reference(self.system_number + "/System_Variables/passedMaskDetection", self.app)
        return ref.get()
    
    def get_runDetection(self):
        ref = db.reference(self.system_number + "/System_Variables/runDetection", self.app)
        return ref.get()
    
    def update_currentUser(self, name):
        ref = db.reference(self.system_number + "/System_Variables", self.app)
        ref.update({
            'currentUser' : name,
            'runDetection' : 'true'
        })

    def log_failed_user(self, date, current_user, reason_for_failure) :
        print("logging failed user")
        ref = db.reference(self.system_number + "/Failed_Screenings", self.app)
        ref.child(date).set({
                current_user : {
                    "reasonForFailure" : reason_for_failure
                }
        })