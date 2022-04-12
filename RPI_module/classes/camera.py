from picamera import PiCamera
from time import sleep

class Camera:

    def __init__(self):
        #returns camera instance
        self.camera = PiCamera()
        
    def die(self):
        self.camera.close()
        
    #takes in camera instance and preview time
    #displays camera preview for the indicated amoutn of time
    def camera_preview(self, camera, preview_time):
        camera.start_preview(alpha=200)
        sleep(preview_time)
        camera.stop_preview()

    #takes in camera instance and degrees
    #rotates camera to indicated degree
    def rotate_camera(self, degrees):
        self.camera.rotation = 180
        
    #takes in camera instance, output image location, countdown time and preview boolean .
    #If preview is true, preview is started
    # the code wats the indicated countdown time before the image ist aken and stored in the indicated location
    # the preview is stopped if it was started
    def capture_image(self, image_out_location, image_name, countdown_time = 0, preview = False):
        if preview:
            self.camera.start_preview()
        
        sleep(countdown_time)
        self.camera.capture(image_out_location + image_name) # + ""
            
        if preview:
            camera.stop_preview()
    