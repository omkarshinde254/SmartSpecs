import os
import numpy as np
import cv2
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer();
path='DataSet'

def getImagesWithId(path):
    imagePaths = [os.path.join(path , f) for f in os.listdir(path) ]
    faces = []
    ids = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg , 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print (ids)
        ids.append(ID)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return faces , np.array(ids)


faces,ids = getImagesWithId(path)

recognizer.train(faces , ids)
recognizer.save('recognizer/TranningData.yml')
cv2.destroyAllWindows()


        
