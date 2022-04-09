# Covid Rapid Screener
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

### Installation of dependencies

## Confirmation of installation