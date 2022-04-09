# Covid Rapid Screener
# ![Covid Rapid Screener](https://929687.smushcdn.com/2633864/wp-content/uploads/2020/04/face_mask_detection_result01.jpg?lossy=1&strip=1&webp=1)

## Group number: L3W-G4
## Student names:
- Alexandre Janelle-Goode, 101138523
- Seneli Seneviratne, 101114455
- Deji Sayomi, 100847393
## TA name: Roger Selzler
## Course: SYSC3010
## What is the Covid Rapid Screener?

The Covid Rapid Screener is a embeded system that verifies that a person is correctly wearing their mask and that their body temperature is below 38 degrees celsius.

The system is composed of four different software modules: the GUI, cloud database (Firebase), Mask Detection module and the Raspberry Pi module. These modules communicate with each other using the cloud database.

The Hardware used to create the system is a Raspberry Pi, MLX90640 IR Thermal Camera, Piezo Buzzer and the Raspberry Pi Camera V2.

## Description of the Repo

### [Face-Mask-Detection](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/Face-Mask-Detection)
The code located here is responsible for the mask detected module of this system.

### [RPI_module] needs link
The code located here is responsible for the Raspberry Pi module of this system. In this folder, there is code for each hardware component located in the "classes" folder.

### [Client](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/client)
The code located here is resposible for the GUI.

### [Unit-Tests](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/Unit-Tests)
The code located here is responsible for testing each module. The possible test are: 

- [thermal camera](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/thermal-camera-advanced.py)

- [firebase](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/test_covidRapidScreener)

- [buzzer](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/test_buzzer.py)

- [mask detector](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/DetectorTest/detect_mask_pictureTEST.py)

### [end-to-end](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/end-to-end)
This code is used to show that connection and communication can be established between the modules.

### [WeeklyUpdates](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/WeeklyUpdates)
This folder contains the work that each group member has done in the week, their weekly goal and opinions of the work that has been accomplished in that week.

## Installation instructions

### Installation of hardware components

List of hardware needed:
- [Raspberry Pi 4](https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/)
- [MLX90640 IR Thermal Camera by adafruit.](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4469/11497511?s=N4IgTCBcDaIIwFYwA4C0AWdA2AnKgcgCIgC6AvkA) Either 55 degree or 110 degree version
- [Piezo Buzzer](https://www.digikey.ca/en/products/detail/murata-electronics/PKM22EPPH2001-B0/1219322?s=N4IgTCBcDaICwE4AMBaOA2BBGFA5AIiALoC%2BQA)
- [Raspberry Pi Cam V2](https://www.pishop.ca/product/raspberry-pi-8mp-camera-board-v2/?src=raspberrypi)

Strongly suggest, but optional:
- [STEMMA QT / Qwicc JST SH 4-pin to male Headers Cable](https://www.adafruit.com/product/4209)

#### To install the Thermal Camera:

If using the STEMMA QT Qwicc connector
- plug in the Qwicc connector into the IR camera
- connect red wire to a 3.3VDC pin on the raspberry pi
- connect black wire to ground pin on the raspberry pi
- connect blue wire to I2C SDA Data pin (pin 3) on the raspberry pi
- connect yellow to I2C SCL Clock pin (pin 5) on the raspberry pi

#### Packages to install to Raspberry Pi for the Thermal Camera
- sudo apt install python3-matplotlib python3-scipy python3-numpy
- sudo apt install python-smbus i2c-tools
- sudo pip3 install RPI.GPIO adafruit-blinka
- sudo pip3 install adafruit-circuitpython-mlx90640

To ensure the camera is properly detected by the raspberry pi, run the following command in the terminal
- sudo i2cdetect -y 1

#### To install the Raspberry PiCam
[For a tutorial with pictures visit this link](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
##### Quick tutorial:
- Shut down the Raspberry Pi
- Locate the Camera Module port
- Gently pull up on the edges of the port’s plastic clip
- Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.
- Push the plastic clip back into place
- Start up the Raspberry Pi
- Go to the main menu and open the Raspberry Pi Configuration tool
- Select the Interfaces tab and ensure that the camera is enabled

#### To install the Buzzer
- Connect the negative end of the buzzer to a ground pin on the raspberry pi
- Connect the positive end of the buzzer to any GPIO pin on the raspberry pi. 17 is suggested for this system.

## How to run the system.
### How to start the RPI_module
- Make sure that the firebase.json has the information of your firebase
- In [RPI_module/classes/firebase.py](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/RPI_module/classes/firebase.py) change line 15, 16, 17 to has the information to your firebase
- in [RPI_module/classes/SMTP.py](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/RPI_module/classes/SMTP.py) change line 7, the receivers to your chosen email(s)
- Run [RPI_module/main.py](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/RPI_module/main.py)
This will be constantly looping for a change in "runDetection" to be "true". Once it is true it will take pictures and upload it to storage, wait for mask detection to change the variable of "passMaskDetection". If "passedMaskDetection" is true then it will check for the temperature. If passedTempDetection is true, delete all pictures. If any of the tests failed, it will save the reason why in firebase and send an email to the email was chosen.

### How to start the GUI
- Seneli write this part please :)

### How to start the Mask Detector
- Deji write this part please :)

## Confirmation of installation
### Confirmation of installation of the Thermal Camera
- First check if the raspberry pi sees the thermal camera
	- Run this line in the terminal: sudo i2cdetect -y 1
	- If it is correctly seen, then "33" should be seen in the "3" column and "30" row
- If that is present, then [run the code found in the Unit-Test folder named thermal-camera-advanced.py](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/thermal-camera-advanced.py). This will give you a live time feed of what the camera sees
- Idealy have something with a known temperature close to you to test the camera.

### Confirmation of installation of the Pi Camera
- Need to find what code tests this

### Confirmation of installation of the buzzer
- [Run the code found in Unit-Test folder named test_buzzer.py](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/test_buzzer.py)
- The buzzer should turn on and off each second

### Confirmation of installation of the GUI
- Seneli please finish this part :)

### Confirmation of installation of the Mask Detector
- Deji please finish this part :)