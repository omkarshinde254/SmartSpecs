import cv2
import numpy as np
#import win32com.client as wincl
import sqlite3
import PIL
import pytesseract
import numpy as np
import pyttsx3


engine = pyttsx3.init()



#-----------------------------------Face Recog------------------

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

recognizer = cv2.face.createLBPHFaceRecognizer();
recognizer.load("recognizer//TranningData.yml")


def getProfile(id):
    conn = sqlite3.connect("FaceDataBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor = conn.execute(cmd)

    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile



capcount = 0
while True :
    ret, image = cap.read()
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,225,0), 5)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])

        profile = getProfile(id)
        if(profile!= None ):
            cv2.putText(image,str(profile[1]), (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 2, 255,3)
    
    
#---------------------------------------------capture-----------

        if cv2.waitKey(1)& 0xFF == ord('c'):
        	cv2.imwrite('captured.jpg',image)
        	capcount =+ 1
        break
        

#---------------------------------show frame------------------------------

    cv2.imshow('face',image)  
    if capcount>=1:
      from PIL import Image


#------------------------------------Get Pic-----------
#cam = cv2.VideoCapture(0)




#---------------------------------grayscaling-----------
      cap_img = cv2.imread('captured.jpg')
      gray_image = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
      cv2.imwrite('gray_cap.jpg',gray_image)
#-------------------------------------thresholding---------
      img = cv2.imread('gray_cap.jpg',0)
      img = cv2.medianBlur(img,5)

      thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

      thr_img = Image.fromarray(thr)
      thr_img.save('thresholdImage.jpg')


      im = Image.open('thresholdImage.jpg')
      im.show()



      text = pytesseract.image_to_string(im)

      print(text)



#------------------------------------------------------------
#---------------------------Speech---------------------------

      rate = engine.getProperty('rate')
      engine.setProperty('rate', rate-50)
      engine.say(text)

      engine.runAndWait()
     


#--------------------------------------------------------

    if(cv2.waitKey(1)==ord('q')):
    	break;
    
cap.release()
cv2.destroyAllWindows()


