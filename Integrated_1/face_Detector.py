import cv2
import numpy as np
import pyttsx3
#import win32com.client as wincl
import sqlite3
import signal
signal.alarm(20)

#---------------pyttsx rate------------------
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-65)

#--------face cascade---------------------------------

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

recognizer = cv2.face.createLBPHFaceRecognizer();
recognizer.load("recognizer//TranningData.yml")

#----------------create a list----------------
names = []
counter = 0
#---------------------create a function---------------
def getProfile(id):
    conn = sqlite3.connect("FaceDataBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor = conn.execute(cmd)

    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile




while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #-------------------------------------------predict------------- call function---------
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 5)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])

        profile = getProfile(id)
        if(profile!= None ):
            cv2.putText(image,str(profile[1]), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 2, 255,3)
#--------------put elements in list and purrn then out-----------

            names.append(profile[1])
            s = list(set(names))
            print (s)
            counter +=1

        

    cv2.imshow('face',image)
    if(cv2.waitKey(1)==ord('q') or counter>=50):
        break;
    
#--------speak it------------
engine.say(s)
engine.runAndWait()
#----------------------------
cap.release()
cv2.destroyAllWindows()
