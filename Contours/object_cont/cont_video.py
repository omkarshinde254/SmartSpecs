import cv2 

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
cap = cv2.VideoCapture(0)

while True:
    # reads frames from a camera
    ret, frame = cap.read()
 
    # converting to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #edged = cv2.Canny(gray, 10, 250)
    
     
    #thresh = cv2.threshold(gray, 127, 255, 0)
    #blur = cv2.medianBlur(gray,5)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    #ret, ti = cv2.bitwise_not(thresh)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
   

    _, contours, _= cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, 2, (0,255,0), 3)

    cv2.imshow('countour', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('thresh', thresh)
    cv2.imshow('closed', closed)

    if cv2.waitKey (1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows() 
