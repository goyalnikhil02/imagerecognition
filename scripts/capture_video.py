import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while(True):
    tf,frame = cam.read()
    print(tf)
    cv2.imshow('Single frame',frame)
    key = cv2.waitKey(0)
    if key == 27:
        print(key)
        break
    
cam.release()
cv2.destroyAllWindows()    
