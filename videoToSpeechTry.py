import PIL
import pytesseract
import cv2
import numpy as np


from espeak import espeak

from PIL import Image


cam = cv2.VideoCapture(0)

while True:
	ret,img = cam.read()
	cv2.imshow('livefeed',img)
	#if cv2.waitKey(1)& 0xFF == ord('c'):
	#	cv2.imwrite('captured.jpg',img)

	if cv2.waitKey(1)& 0xFF == ord('q'):
		cv2.imwrite('captured.jpg',img)
		break

cam.release()
cv2.destroyAllWindows()
#---------------------------------grayscaling-----------
cap_img = cv2.imread('captured.jpg')
gray_image = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_cap.jpg',gray_image)
#-------------------------------------thresholding---------
img = cv2.imread('thresholdImage1.jpg',0)
img = cv2.medianBlur(img,5)

thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

thr_img = Image.fromarray(thr)
thr_img.save('thresholdImage.jpg')


im = Image.open('thresholdImage.jpg')
im.show()



text = pytesseract.image_to_string(im)

print(text)


#------------------------------------------------------

#espeak.set_parameter(espeak.Parameter.Rate, 120)

#espeak.synth(text) 
#while espeak.is_playing:
#	pass



#--------------------------------------------------------








	



