import cv2
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


def InsertOrUpdate(Id,Name):
    conn = sqlite3.connect("FaceDataBase.db")
    cmd = " SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    IfRecordExist = 0
    for row in cursor:
         IfRecordExist = 1
    if(IfRecordExist):
        cmd = " UPDATE People SET Name="+str(Name)+" WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO People (ID,Name) Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    

id = input('Enter The User ID')
name = input('Enter Your Name')
InsertOrUpdate(id,name)
SampleNumber=0

while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        SampleNumber = SampleNumber+1
        

        
        cv2.imwrite("DataSet/User."+str(id)+"."+str(SampleNumber)+".jpg",gray[y:y+h,x:x+h])
        cv2.waitKey(100)
        
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 2)
        
    cv2.imshow('face',image)
    cv2.waitKey(1)

    if(SampleNumber>20):
        break
    
    


cap.release()
cv2.destroyAllWindows()
