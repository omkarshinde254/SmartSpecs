import cv2
import numpy as np
from PIL import Image

im =  cv2.imread('book.jpg')
gray = cv2.cvtColor(im , cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray,127,255,0)

_, contours, _= cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



cv2.drawContours(im , contours ,-1,(0,255,0),3)



cv2.imshow("Contours",im)
cv2.waitKey(0)
