import cv2 

cap = cv2.VideoCapture(0)

while True:
    # reads frames from a camera
    ret, frame = cap.read()
 
    # converting to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    #thresh = cv2.threshold(gray, 127, 255, 0)
    blur = cv2.medianBlur(gray,5)
    ret, thresh = cv2.threshold(blur, 127, 255, 0)
   

    _, contours, _= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

    cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    cv2.imshow('countour', frame)

    if cv2.waitKey (1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows() 
