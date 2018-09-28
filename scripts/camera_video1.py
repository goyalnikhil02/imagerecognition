import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while(True):
    tf,frame = cam.read()
    #print(tf)
    ## to change the video framwe in grey color
   # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Single frame',frame)
    key = cv2.waitKey(0)## it will keep on
    if key == 27:
        print(key)
        break
    elif key ==ord('x'):
        print ('you have letter x')
        break
    
cam.release()
cv2.destroyAllWindows()    
