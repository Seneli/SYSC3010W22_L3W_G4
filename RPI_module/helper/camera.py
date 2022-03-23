from picamera import PiCamera
from time import sleep

class Camera:

    def __init__(self):
        #returns camera instance
        self.camera = PiCamera()
        
    #takes in camera instance and preview time
    #displays camera preview for the indicated amoutn of time
    def camera_preview(self, camera, preview_time):
        camera.start_preview(alpha=200)
        sleep(preview_time)
        camera.stop_preview()

    #takes in camera instance and degrees
    #rotates camera to indicated degree
    def rotate_camera(self, camera, degrees):
        camera.rotation(degrees)
        
    #takes in camera instance, output image location, countdown time and preview boolean .
    #If preview is true, preview is started
    # the code wats the indicated countdown time before the image ist aken and stored in the indicated location
    # the preview is stopped if it was started
    def capture_image(self, camera, image_out_location, countdown_time = 0, preview = False):
        if preview:
            camera.start_preview()
        
        sleep(countdown_time)
        camera.capture(image_out_location) # + ""
            
        if preview:
            camera.stop_preview()
    