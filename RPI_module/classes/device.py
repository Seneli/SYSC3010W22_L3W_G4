from datetime import datetime
import os

# custom imports
from firebase import FireBase
from camera import Camera


class Device:
    
    def __init__(self, system_number=1, owner="L3W_G4", contact_info="L3W.G4.SAD@gmail.com"):
        self.system_number = system_number
        self.owner = owner
        self.contact_info = contact_info
        self.firebase = FireBase(system_number)
        self.camera = Camera()
        print(system_number, owner, contact)
        
        
    def user_failed_screening(self, system_variables, firebase):
        date = datetime.today().strftime('%Y-%m-%d')
        
        reason_for_failure = ""
        if system_variables["passedMaskDetection"] == 'false':
            reason_for_failure = "failed mask detection"
        elif system_variables["passedTempDetection"] == 'false':
            reason_for_failure = "failed temperature detection"
            
        return date, reason_for_failure
        
    def take_pictures_for_mask_detection():
        pass
    
    def wait_for_mask_detection_module_to_finish():
        pass
    
    def run_temperature_sensor_module():
        pass
        print("run temperature sensing stuff")
        print("check if it failed")
    
    def delete_all_pictures_and_reset(firebase):
        os.rmdir("/images")
        os.mkdir("/images")

    def run():
        self.firebase.initialize_rtdb_datastruct()

        while(True):

            sys_var = firebase.get_System_Variables()

            if sys_var['runDetection'] == "true":
                
                #run mask detection 
                for i in range(10):
                    print("PiCam takes picture")
                        ## TEST IF CAMERA TAKES PICTURE
                        ## TEST IF CAMERA DELETES PICTURE FROM LOCAL
                    #camera.capture_image(cam, "/images")
                    #insert image upload code here
                    firebase.put_image_in_storage(i+".jpg", "images/ml1.jpg")

                    passedMaskDetection = firebase.get_passedMaskDetection()
                    if passedMaskDetection == "true":
                        break 
                    elif passedMaskDetection == "false":
                        user_failed_screening(sys_var)
                    else:
                        pass
                
                while(passedMaskDetection == "null"): #null = keep polling
                    passedMaskDetection = get_passedMaskDetection()
                    if passedMaskDetection == "true":   # true = next test
                        break
                    elif passedMaskDetection == "false": #false = failed test
                        user_failed_screening(sys_var)
                        break

            #run temperature detection
            sys_var = self.firebase.get_System_Variables()
            if sys_var["runDetection"] == "true":
                pass

            delete_all_pictures_and_reset(firebase) 
            # once it passes - delete all pictures in storage
