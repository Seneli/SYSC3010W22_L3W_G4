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
The code located here is responsible for the Raspberry Pi module of this system.

### [Unit-Tests](https://github.com/Seneli/SYSC3010W22_L3W_G4/tree/main/Unit-Tests)
The code located here is responsible for testing each module. The possible test are: 

- [thermal camera](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/thermal-camera-advanced.py)

- [firebase](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/test_covidRapidScreener)

- [buzzer](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/test_buzzer.py)

- [mask detector](https://github.com/Seneli/SYSC3010W22_L3W_G4/blob/main/Unit-Tests/DetectorTest/detect_mask_pictureTEST.py)

### WeeklyUpdates
### Client
### end-to-end

## Installation instructions

## Confirmation of installation