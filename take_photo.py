from picamera import PiCamera
from time import sleep
from datetime import datetime
import numpy as np
import cv2
import os
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDTVhzWm61yvueMdj7XGnHhmWikSgbWti0",
 'authDomain': "visiting-f94b9.firebaseapp.com",
 'databaseURL': "https://visiting-f94b9-default-rtdb.firebaseio.com",
 'projectId': "visiting-f94b9",
 'storageBucket': "visiting-f94b9.appspot.com",
 'messagingSenderId': "458919562545",
 'appId': "1:458919562545:web:ea4cedf898f67fee83f410",
 'measurementId': "G-12E5X2TGW0"

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

camera = PiCamera()

camera.start_preview()

name = "person1.jpg"
name1="person2.jpg"
name2="person3.jpg"
name3="person4.jpg"
name4="person5.jpg"
name5="person6.jpg"
name6="person7.jpg"
name7="person8.jpg"
name8="person9.jpg"
name9="person10.jpg"


camera.capture(name)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person1.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name).put(name)
    print("image sent")
    os.remove(name)

camera.start_preview()
camera.capture(name1)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person2.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name1).put(name1)
    print("image sent")
    os.remove(name1)
    
camera.start_preview()
camera.capture(name2)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person3.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name2).put(name2)
    print("image sent")
    os.remove(name2)

camera.start_preview()
camera.capture(name3)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person4.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name3).put(name3)
    print("image sent")
    os.remove(name3)
cv2.destroyAllWindows()

camera.start_preview()
camera.capture(name4)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person5.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name4).put(name4)
    print("image sent")
    os.remove(name4)

camera.start_preview()
camera.capture(name5)
sleep(5)
camera.stop_preview()
classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('/home/pi/person6.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")
for(x,y,w,h) in face_roi:
    storage.child(name5).put(name5)
    print("image sent")
    os.remove(name5)