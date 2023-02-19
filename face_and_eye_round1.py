import cv2	
import numpy as np

face_cascade = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('dataset/haarcascade_eye.xml')



cap = cv2.VideoCapture(0)

while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 6)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = image[y:y+h , x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
        	cv2.rectangle(roi_color, (ex,ey) , (ex+ew,ey+eh) , (0,225,255), 2)



    cv2.imshow('face',image)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    


cap.release()
cv2.destroyAllWindows()
