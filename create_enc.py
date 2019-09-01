# -*- coding: utf-8 -*-
import dlib
import face_recognition
from imutils import paths

import cv2
import pickle
import os
print(dlib.DLIB_USE_CUDA) # See readme.md file for info

imagePaths = list(paths.list_images('dataset'))
knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):
	print('[INFO] Processing image {}/{}'.format(i+1, len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(rgb, model='hog')  # Use hog or cnn. Only use cnn if you have enough processing power

	encodings = face_recognition.face_encodings(rgb, boxes)

	for encoding in encodings:
		knownEncodings.append(encoding)
		knownNames.append(name)
	print('[INFO] Storing encodings...')
	data = {'encodings':knownEncodings, 'names':knownNames}
	f = open('encodings.pickle', 'wb')
	f.write(pickle.dumps(data))
	f.close()

import face_recognition 
import cv2
import pickle


print("[INFO] loading encodings...")
data = pickle.loads(open('encodings.pickle', "rb").read())
image = cv2.imread('examples/example_01.png')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb, model='hog') 
encodings = face_recognition.face_encodings(rgb, boxes)

matches = []

for encoding in encodings:
	matches = face_recognition.compare_faces(data['encodings'], encoding)
count = 0
for i in matches:
	if i == True:
		count += 1
print((count/30)*100)   # Just to see a measure of how good the model is.

