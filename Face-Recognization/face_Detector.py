import cv2
import numpy as np
#import time
#import win32com.client as wincl


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
#time.sleep(2)

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("recognizer//TranningData.yml")


id=0


while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 2)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="omkar"

        cv2.putText(image,str(id), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 2, 255,3)

        

    cv2.imshow('face',image)
    if(cv2.waitKey(1)==ord('q')):
        break;
    
#print(id) 
#speak = wincl.Dispatch("SAPI.SpVoice")
#speak.Speak(id)

cap.release()
cv2.destroyAllWindows()
