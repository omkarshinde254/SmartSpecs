import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 2)
        

    cv2.imshow('face',image)
    if(cv2.waitKey(1)==ord('q')):
        break;
    


cap.release()
cv2.destroyAllWindows()
