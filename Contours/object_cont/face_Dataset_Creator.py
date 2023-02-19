import cv2
import numpy as np


cap = cv2.VideoCapture(0)


id = input('Enter The User ID')
SampleNumber=0

while True :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)
    ret, thresh = cv2.threshold(blur, 127, 255, 0)
    _, contours, _= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

    for (x,y,w,h) in contours:
        SampleNumber = SampleNumber+1
        

        
        cv2.imwrite("DataSet/User."+str(1)+"."+str(SampleNumber)+".jpg",gray[y:y+h,x:x+h])
        cv2.waitKey(100)
        
        cv2.drawContours(frame, contours, -1, (0,255,0), 3)
        
    cv2.imshow('countour', frame)
    cv2.waitKey(1)

    if(SampleNumber>20):
        break
    
    


cap.release()
cv2.destroyAllWindows()
