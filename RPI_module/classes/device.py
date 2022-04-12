from datetime import datetime
import os

# custom imports
from classes.firebase import FireBase
from classes.camera import Camera
from classes.thermalCam import ThermalCam
from classes.buzzer import MyBuzzer
from classes.SMTP import EmailSender

# Make connection with firebase
# Make connections to all devices
# (camera, IR camera, buzzer, mask_detection module)
# Continuously poll firebase for variables
# react to the changes of variables
# reaction changed depending on the variables


class Device:
    def __init__(self, system_number=1, owner="L3W_G4",
                 contact_info="L3W.G4.SAD@gmail.com"):
        self.system_number = system_number
        self.owner = owner
        self.contact_info = contact_info

        self.firebase = FireBase(system_number)
        self.firebase.initialize_rtdb_datastruct()
        
        self.emailSender = EmailSender()

        self.camera = Camera()
        self.thermalCam = ThermalCam()
        self.myBuzzer = MyBuzzer(17)
        
        self.running = False
        self.currentTest = "waiting"
        self.sys_var = {}

    def die(self):
        self.firebase.die()
        self.camera.die()
        self.emailSender.die()

    def user_failed_screening(self):
        system_variables = self.firebase.get_System_Variables()
        date = datetime.today().strftime('%Y-%m-%d')

        reason_for_failure = ""
        if system_variables["passedMaskDetection"] == 'false':
            reason_for_failure = "failed mask detection"
        elif system_variables["passedTempDetection"] == 'false':
            reason_for_failure = "failed temperature detection"

        self.firebase.log_failed_user(date, system_variables["currentUser"], reason_for_failure) 
        self.emailSender.create_and_send_email(system_variables["currentUser"], reason_for_failure)

    def take_pictures_for_mask_detection(self):
        for i in range(10):
            self.camera.rotate_camera(180)
            self.camera.capture_image("./images/", str(i) + ".jpg")
            self.firebase.put_image_in_storage(self.system_number, str(i) + ".jpg")

            passedMaskDetection = self.firebase.get_passedMaskDetection()

            if passedMaskDetection == "true":
                self.currentTest = "temp"
                break

            elif passedMaskDetection == "false":
                self.user_failed_screening()
                self.running = False
                self.currentTest = ""
                break

    def wait_for_mask_detection_module_to_finish(self):
        sys_var = self.firebase.get_System_Variables()
        passedMaskDetection = self.firebase.get_passedMaskDetection()
        while(passedMaskDetection == "null"):  # null = keep polling
            passedMaskDetection = self.firebase.get_passedMaskDetection()
            if passedMaskDetection == "true":   # true = next test
                self.currentTest = "temp"
                break
            elif passedMaskDetection == "false":  # false = failed test
                print("passed false")
                self.myBuzzer.buzz()
                self.user_failed_screening()
                self.currentTest = "none"
                self.firebase.set_runDetection("false")
                break

    def run_temperature_sensor_module(self):
        sys_var = self.firebase.get_System_Variables()
        print("getting temperature")
        self.firebase.set_detectedTemp("Getting Temperature")
        temp = self.thermalCam.get_avg_temp()
        if (temp > 38):
            print("Temperature is above 38 degrees celsius")
            self.firebase.set_passedTempDetection("false")
            self.firebase.set_detectedTemp(str(temp))
            self.user_failed_screening() # move this to else statement when almost done
            self.myBuzzer.buzz()
        else:
            print("Temperature is under 38 degrees celsius")
            self.firebase.set_passedTempDetection("true")
            self.firebase.set_detectedTemp(temp)

    def delete_all_pictures_off_local(self, folder):
        for file in os.listdir(folder):
            os.remove(folder + "/" + file)
            

    def run(self):
        self.running = True
        print("device now running")

        while(True):
            sys_var = self.firebase.get_System_Variables()
            print(sys_var)
            if sys_var['runDetection'] == "true":
                print("run mask detection tests")

                self.currentTest = "mask"
                self.take_pictures_for_mask_detection()
                print("pictures taken")
                self.wait_for_mask_detection_module_to_finish()
                self.firebase.set_runDetection("false")

            if self.currentTest == "temp":
                self.run_temperature_sensor_module()
                self.currentTest = "none"

            if self.currentTest == "none":
                print("delete all pictures off local")
                self.delete_all_pictures_off_local("images")
                self.currentTest = "waiting"
                

# Flake8 output:
# nothing
