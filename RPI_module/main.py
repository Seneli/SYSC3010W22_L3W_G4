from datetime import datetime
import os

# custom imports
from helper.firebase import FireBase
#import camera as camera

# global variables
system_number = "001"


def user_failed_screening(system_variables, firebase):
    print("put their name in the failed list")
    date = datetime.today().strftime('%Y-%m-%d')
        # do test for date and time? 

    reason_for_failure = ""

    if system_variables["passedMaskDetection"] == 'false':
        reason_for_failure = "failed mask detection"
    elif system_variables["passedTempDetection"] == 'false':
        reason_for_failure = "failed temperature detection"

def delete_all_pictures_and_reset(firebase):
    os.rmdir("/images")
    os.mkdir("/images")

def main():
    firebase = FireBase("001", True)
    firebase.initialize_rtdb_datastruct()

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
        sys_var = firebase.get_System_Variables()
        if sys_var["runDetection"] == "true":
            print("run temperature sensing stuff")
            print("check if it failed")

        delete_all_pictures_and_reset(firebase) 
        # once it passes - delete all pictures in storage

 
        


if __name__ == "__main__":
    print("RPI Module starting...")
    main()
