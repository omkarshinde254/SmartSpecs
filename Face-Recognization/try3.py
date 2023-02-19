import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
path = 'DataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    print (imagePaths)

getImagesWithID(path)
