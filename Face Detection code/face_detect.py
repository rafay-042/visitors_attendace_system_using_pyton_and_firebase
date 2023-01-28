import numpy as np
import cv2

classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('/home/pi/tmg.jpg',1)
grayscale_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_roi = classify_face.detectMultiScale(grayscale_img, 1.3,5)

if face_roi is ():
    print("Faces are not Detected, please provide another image")

for(x,y,w,h) in face_roi:
    cv2.rectangle(img, (x,y), (x+w, y+h), (127,0,255), 2)
    
    
    cv2.imshow('Face Detection Result', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()