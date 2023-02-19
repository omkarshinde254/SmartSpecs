import cv2
from PIL import Image
import numpy as np

img = cv2.imread("captured.jpg", 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)

print ("Threshold selected : ", ret)
cv2.imwrite("./debug.png", thresh)

thr_img = Image.fromarray(thresh)
thr_img.save('thresholdImage1.jpg')


im = Image.open('thresholdImage1.jpg')
im.show()
