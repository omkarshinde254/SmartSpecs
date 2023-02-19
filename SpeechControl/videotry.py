import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    
    cv2.imshow('Coloured ME',frame)
    cv2.imshow('Grayscale ME', gray)

    if cv2.waitKey (1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
