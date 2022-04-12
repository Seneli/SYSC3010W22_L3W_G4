from picamera import PiCamera
from time import sleep

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        
    def die(self):
        self.camera.close()
        
    def rotate_camera(self, degrees):
        self.camera.rotation = 180

    def capture_image(self, image_out_location, image_name, countdown_time = 0, preview = False):
        if preview:
            self.camera.start_preview()
        
        sleep(countdown_time)
        self.camera.capture(image_out_location + image_name) 
            
        if preview:
            camera.stop_preview()
    