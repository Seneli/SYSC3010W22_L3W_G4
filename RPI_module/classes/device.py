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
        
        #self.IR_camera = asdasd
        
        self.running = False
        self.currentTest = "waiting"
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
            self.firebase.put_image_in_storage(str(i)+".jpg", str(i)+".jpg")

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
        passedMaskDetection = self.firebase.get_passedMaskDetection()
        while(passedMaskDetection == "null"): #null = keep polling
            passedMaskDetection = self.firebase.get_passedMaskDetection()
            if passedMaskDetection == "true":   # true = next test
                self.currentTest = "temp"
                break
            elif passedMaskDetection == "false": #false = failed test
                user_failed_screening(sys_var)
                self.currentTest = "none"
                break
    
    def run_temperature_sensor_module(self):
        pass
        print("run temperature sensing stuff")
        print("check if it failed")
    
    def delete_all_pictures_off_local(self, folder):
        for file in os.listdir(folder):
            os.remove(folder + "/" + file)

    def run(self):
        self.firebase.delete_image_from_storage("image.jpg")
        self.firebase.delete_bucket_from_storage("./")
        """
        self.running = True
        print("device now running")

        while(self.running):

            sys_var = self.firebase.get_System_Variables()

            if sys_var['runDetection'] == "true":
                print("run mask detection tests")
                
                self.currentTest = "mask"
                self.take_pictures_for_mask_detection()
                print("pictures taken")
                self.wait_for_mask_detection_module_to_finish()
            
            if self.currentTest == "temp":
                print("run temperature tests")
                self.currentTest = "none"
                
            if self.currentTest == "none":
                print("delete all pictures off local")
                self.delete_all_pictures_off_local("images")
                self.currentTest = "waiting"
                self.running = False
        """