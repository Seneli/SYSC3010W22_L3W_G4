from gpiozero import Buzzer
from time import sleep

class MyBuzzer:
    
    def __init__(self, pin):
        self.myBuzzer = Buzzer(17)

    def buzz(self):
        self.myBuzzer.on()
        sleep(1)
        self.myBuzzer.off()
