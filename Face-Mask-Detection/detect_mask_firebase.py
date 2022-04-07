"""
Background: The COVID Rapid Screener project from group L3W_G4-SYSC_3010_A-
Winter_2022 determines if a user is correctly wearing a mask for campus 
building access privileges. To do this a camera takes 10 pictures of the 
user in rapid succession and loads it into Firebase storage. Then this 
file takes those 10 pictures and runs them throught the the mask detection
code below.  

In each image, if the user is correctly wearing a mask, a box will appear 
around their face and flash green. If they are not wearing a mask correctly a 
red box will flash around their face. If 6 or more of those images show the
user is correctly wearing a mask, they will pass the mask detection. 

A separate file, called train_mask_detector.py trains the mask detection
model by taking in a folder containing images of people wearing a mask
correctly and a folder containing images of people not wearing a mask
correctly. The trained model areoutput files called: 
face_detector\deploy.prototxt and 
face_detector\res10_300x300_ssd_iter_140000.caffemodel. 

This file refers to those files to determine whether the mask is being 
correctly worn or not.  

This code is based on the face mask detection algorithm by Balaji Srinivasan.
Github: https://github.com/balajisrinivas/Face-Mask-Detection
YouTube: https://www.youtube.com/watch?v=Ax6P93r32KU&t=1s 
"""

# Import the necessary packages
from cv2 import COLOR_BGR2BGR555
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np 
import imutils
import cv2


def detect_and_predict_mask(frame, faceNet, maskNet):
	# Grab the dimensions of the frame and then construct a blob
	# from it
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
		(104.0, 177.0, 123.0))

	# Pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()
	print(detections.shape)

	# Initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	faces = []
	locs = []
	preds = []

	# Loop over the detections
	for i in range(0, detections.shape[2]):
		# Extract the confidence (i.e., probability) associated with 
		# the detection
		confidence = detections[0, 0, i, 2]

		# Filter out weak detections by ensuring the confidence is
		# greater than the minimum confidence
		if confidence > 0.5:
			# Compute the (x, y)-coordinates of the bounding box for
			# the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# Ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# Extract the face ROI, convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# Add the face and bounding boxes to their respective
			# lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# Only make a predictions if at least one face was detected
	if len(faces) > 0:
		# For faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# Return a 2-tuple of the face locations and their corresponding
	# locations
	return (locs, preds)


def put_image_in_storage(image_name_on_storage, image_name_on_local):
    blob = storage.bucket().blob(image_name_on_storage)
    blob.upload_from_filename(image_name_on_local)



# Load our serialized face detector model from disk
prototxtPath = r"face_detector\deploy.prototxt"
weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# Load the face mask detector model from disk
maskNet = load_model("mask_detector.model")

# The paragraph of code below handles communication with: 1. The 
# firebase database to access 'System_Variables'; and 2. The
# firebase storage to access images. 
cred = credentials.Certificate('rapid_screener_certificate.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://covid-rapid-screener-default-rtdb.firebaseio.com/',
	'storageBucket': 'covid-rapid-screener.appspot.com'
})


print("\n[INFO] Waiting for Rapid Screener to run mask detection")

# Run infinite loop waiting for runMaskDetection insystem variables 
# to change to "true
while True:
	#To be changed: The unit number of the detection device being used
	unit_number = 1
	
	# Database access
	unit = db.reference(str(unit_number))
	sys_var = unit.child('System_Variables')
	# Get runMaskDetection variable from Firebase and run detection if variable
	# Changes to true
	runDetection = sys_var.child('runDetection').get()

	if runDetection == "true":
		# The for loop below will increase 'passed' when a particular
		# frame passes the mask detection test. Otherwise, 'failed' gets
		# increased. 
		passed = 0
		failed = 0

		print("[INFO] starting samples")
		# Loop over the 10 pictures taken from firebase. Determine if each  
		# frame passes the mask detection. If 6 or more frames pass the detection, 
		# the user has passed the overall mask detection and the detection program 
		# will set the 'passedMaskDetection' variable in Firebase to 'True'. 
		# Otherwise, they have failed and the 'passedMaskDetection' variable will be 
		# set to 'False'.
		
		for i in range(10):
			# Storage access
			bucket  = storage.bucket()
			# The firebase storage path from which to get pictures 
			# from. Ex: "1/0.jpg" or "1/8.jpg" 
			blob_firebase = bucket.get_blob(str(unit_number) + "/" + str(i) + ".jpg")
			# Handle "NoneType" 
			while blob_firebase == None:
				blob_firebase = bucket.get_blob(str(unit_number) + "/" + str(i) + ".jpg")
			arr_firebase = np.frombuffer(blob_firebase.download_as_string(), np.uint8)
			frame = cv2.imdecode(arr_firebase, cv2.COLOR_BGR2BGR555)
			frame = imutils.resize(frame, width=400)

			# Detect faces in the frame and determine if they are wearing a
			# face mask or not
			(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

			# Loop over the detected face locations and their corresponding
			# locations
			for (box, pred) in zip(locs, preds):
				# Unpack the bounding box and predictions
				(startX, startY, endX, endY) = box
				(mask, withoutMask) = pred

				# Determine the class label and color we'll use to draw
				# the bounding box and text
				label = "Mask" if mask > withoutMask else "Put on or adjust mask"
				color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

				# Include the probability in the label
				label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

				# Update whether detection passed or failed
				if mask > withoutMask:
					passed += 1
				else:
					failed += 1

				print("Passed: " + str(passed) + " || Failed: " + str(failed))

				# Display the label and bounding box rectangle on the output
				# frame
				cv2.putText(frame, label, (startX, startY - 10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
				cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

			# Show the output frame
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF

			# Store image of green/red boxed image as jpeg in firebese storage
			cv2.imwrite(str(unit_number) + "_processed_images_local/" + str(i) + ".jpg", frame)
			img_local = str(unit_number) + "_processed_images_local/" + str(i) + ".jpg"
			img_storage = str(unit_number) + "_processed_images/" + str(i) + ".jpg"
			put_image_in_storage(img_storage, img_local)

			# If the `q` key was pressed, break from the loop
			if key == ord("q"):
				break

		# Update system variables. If the user has six or more frames that 
		# passed the test, they have passed the mask detection. Otherwise, 
		# they failed.
		if passed > failed:
			sys_var.update({
				'passedMaskDetection': 'true'
			})
		else:
			sys_var.update({
				'passedMaskDetection': 'false'
			})

		# Reset runDetection to null to break loop
		sys_var.update({
			'runDetection' : 'null'
		})

		#Do a bit of cleanup
		cv2.destroyAllWindows()