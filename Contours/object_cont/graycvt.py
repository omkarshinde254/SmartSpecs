import cv2

n=1
p=10
while True:
	
	cap_img = cv2.imread('User.1.'+str(n)+'.jpg')
	gray_image = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('User.1.'+str(n)+'.jpg',gray_image)
	n = n+1
	p = p+1
