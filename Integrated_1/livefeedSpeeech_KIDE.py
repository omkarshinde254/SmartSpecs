import PIL
import pytesseract
import cv2
import numpy as np
import pyttsx3
from PIL import ImageFilter
from PIL import Image
import time



engine = pyttsx3.init()


#from espeak import espeak

from PIL import Image

#------------------------------------Get Pic-----------
cam = cv2.VideoCapture(0)
ret,img = cam.read()
cv2.imshow('livefeed',img)
time.sleep(3)
cv2.imwrite('captured.jpg',img)

cam.release()
cv2.destroyAllWindows()
#---------------------------Denoising---------------
imgD = cv2.imread('captured.jpg')
dnoise = cv2.fastNlMeansDenoisingColored(imgD,None,10,10,7,21)
imgDnoised = Image.fromarray(dnoise)
imgDnoised.save('dnoised.jpg')
#---------------------------------grayscaling-----------
cap_img = cv2.imread('dnoised.jpg')
gray_image = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_cap.jpg',gray_image)

#------------------------------_Smooothing------------------
imSmooth = Image.open('gray_cap.jpg')
imS = imSmooth.filter(ImageFilter.SMOOTH_MORE)
imS.save('smoothmmmm.jpg')
#-------------------------miniFilter---------------
#imFilter = Image.open('smoothmmmm.jpg')
#imMF = imFilter.filter(ImageFilter.MinFilter)
#imMF.save('minifilter.jpg')
#----------------------------Blur----------
#imBlur = Image.open('smoothmmmm.jpg')
#imB = imBlur.filter(ImageFilter.BLUR)
#imB.save('Blur.jpg')
#----------------------opening---------------
#imOpen = cv2.imread('Blur.jpg')
#kernel = np.ones((2,2),np.uint8)
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#imO = Image.fromarray(opening)
#imO.save('opened.jpg')
#-------------------------------------thresholding---------
img = cv2.imread('smoothmmmm.jpg',0)
img = cv2.medianBlur(img,5)

thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

thr_img = Image.fromarray(thr)
thr_img.save('thresholdImage.jpg')


#----------------------------------------------------


im = Image.open('thresholdImage.jpg')
im.show()



text = pytesseract.image_to_string(im)

print(text)


#---------------------------Speech---------------------------

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

engine.say(text)
engine.runAndWait()


#--------------------------------------------------------








	



