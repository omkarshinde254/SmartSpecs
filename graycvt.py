import cv2

cap_img = cv2.imread('captured.jpg')
gray_image = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_cap.jpg',gray_image)
