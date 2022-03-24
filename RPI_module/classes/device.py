from datetime import datetime
import os

# custom imports
from classes.firebase import FireBase
from classes.camera import Camera


class Device:
    
    def __init__(self, system_number=1, owner="L3W_G4", contact_info="L3W.G4.SAD@gmail.com"):
        self.system_number = system_number
        self.owner = owner
        self.contact_info = contact_info
        
        self.firebase = FireBase(system_number)
        self.firebase.initialize_rtdb_datastruct()
        
        self.camera = Camera()
        
        self.running = False
        self.currentTest = ""
        self.sys_var = {}
        
    
    def die(self):
        self.firebase.die()
        self.camera.die()
        
        
    def user_failed_screening(self):
        system_variables = self.firebase.get_System_Variables()
        date = datetime.today().strftime('%Y-%m-%d')
        
        reason_for_failure = ""
        if system_variables["passedMaskDetection"] == 'false':
            reason_for_failure = "failed mask detection"
        elif system_variables["passedTempDetection"] == 'false':
            reason_for_failure = "failed temperature detection"
            
        firebase.log_failed_user(date, system_variables["currentUser"], reason_for_failure) 
        
    def take_pictures_for_mask_detection(self):
        for i in range(10):
            self.camera.capture_image("./images/", str(i) + ".jpg")
            self.firebase.put_image_in_storage(i+".jpg", "images/"+i+".jpg")

            passedMaskDetection = self.firebase.get_passedMaskDetection()
            
            if passedMaskDetection == "true":
                self.currentTest = "temp"
                break
            
            elif passedMaskDetection == "false":
                user_failed_screening()
                self.running = False
                self.currentTest = ""
                break
            

    def wait_for_mask_detection_module_to_finish(self):
        while(passedMaskDetection == "null"): #null = keep polling
            passedMaskDetection = self.firebase.get_passedMaskDetection()
            if passedMaskDetection == "true":   # true = next test
                break
            elif passedMaskDetection == "false": #false = failed test
                user_failed_screening(sys_var)
                break
    
    def run_temperature_sensor_module(self):
        pass
        print("run temperature sensing stuff")
        print("check if it failed")
    
    def delete_all_pictures_off_local(self):
        os.rmdir("/images")
        os.mkdir("/images")

    def run(self):
        
        self.running = True

        while(self.running):

            self.sys_var = self.firebase.get_System_Variables()

            if self.sys_var['runDetection'] == "true":
                
                self.currentTest = "mask"
                take_pictures_for_mask_detection()
                
                self.running = False
              
            """
                if not self.runnning:
                    break 
                
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
        """