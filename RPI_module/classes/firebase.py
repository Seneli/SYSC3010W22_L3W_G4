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

    def put_image_in_storage(self, sys_num, img_name):
        blob = self.storage.blob(str(sys_num) + "/" + img_name)
        blob.upload_from_filename("./images/" + img_name)
        
    def check_image_exists_in_storage(self, image_name_in_storage):
        pass

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
                "detectedTemp": "null",
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
        
    def set_runDetection(self, boolean):
        ref = db.reference(self.system_number + "/System_Variables", self.app)
        ref.update({
            'runDetection' : boolean,
        })
    
    def set_passedTempDetection(self, boolean):
        ref = db.reference(self.system_number + "/System_Variables", self.app)
        ref.update({
            'passedTempDetection' : boolean,
        })
        
    def set_detectedTemp(self, boolean):
        ref = db.reference(self.system_number + "/System_Variables", self.app)
        ref.update({
            'detectedTemp' : boolean,
        })

    def log_failed_user(self, date, current_user, reason_for_failure) :
        print("logging failed user")
        ref = db.reference(self.system_number + "/Failed_Screenings", self.app)
        ref.child(date).child(current_user).set({
                "reasonForFailure" : reason_for_failure
        })