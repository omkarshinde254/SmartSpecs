import cv2

cam = cv2.VideoCapture(0)

while True:
	ret,img = cam.read()
	cv2.imshow('livefeed',img)
	if cv2.waitKey(1)& 0xFF == ord('c'):
		cv2.imwrite('captured.jpg',img)

	if cv2.waitKey(1)& 0xFF == ord('q'):
		#cv2.imwrite('captured.jpg',img)
		break
cam.release()
cv2.destroyAllWindows()
