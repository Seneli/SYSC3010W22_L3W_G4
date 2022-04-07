# An Overview of Face-Mask-Detection

This folder contains all Relevant source code and files for the mask detection module.

## Files and Folders

### `1_processed_images_local`

This folder contains the 10 pictures taken by the rapid screener camera every time it is used.
These images are then sent to firebase, where they wil be forwarded to the GUI and displayed 
for the user. 

When next the rapid screener is used and new pictures are taken, the 10 pictures in this folder 
are overridden wby the next 10 pictures.

### `face_detector`

When the mask detector module is trained by the train_mask_detector.py file below, two files
(deploy.prototxt and res10_300x300_ssd_iter_140000.caffemodel) are created and stored in this
folder. The detect_mask_firebase.py uses these to files to detect proper application of a face
mask by the user.

### `detect_mask_firebase.py`

This is the active file that is run in order to detect masks. Upon start-up of the rapid 
screener, the this file is then manually run in the terminal. Once up and running no other
manual inputs are required.

The program waits in an infinite loop until a user accesses the the rapid screener. Once the
mask detector is called, it will grab the 10 pictures taken by the rapid screener then detect the 
presence or absence of a mask. It will add a green box (signignifying correct mask application)
or a red box (signifying incorrect or no mask applicaition) to the pictures and store the modified
pictures in the 1_processed_images_local folder. 

From there, the box-modified pictures are sent back to firebase storage where the GUI can take them 
and display on its screen. Meanwhile, detect_mask_firebase.py will update the firebase variable 
passedMaskDetection to 'true' or 'false' depending on whether the user passes the mask detection or not.

### `mask_detector.model`

The detect_mask_firebase.py uses this file to load the face mask detector model from disk.

### 'rapid_screener_certificate.json'

This file specifies the authentication for the rapid screener to access firebase.

### 'requirements.txt'

Specifies all the required packages that need to be installed using pip.

*note: several of these packages are outdated. It is much better to simply install the more 
       recent packages by deleting the version numbers beside each package name.

### 'train_mask_detector.py'

This file trains the model by looking at a images of people in two different folders. The first 
folder (titled with_mask) containins over 1,000 images of people wearing a mask correctly. The 
second folder (titled without_mask) contains over 1,000 images of people wearing a mask incorrectly.

*note: Because these folders are very large, they have not been included in this commit.
