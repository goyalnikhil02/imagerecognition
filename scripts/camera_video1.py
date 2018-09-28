import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while(True):
    tf,frame = cam.read()
    #print(tf)
    ## to change the video framwe in grey color
   # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    upper_red = np.array([130,255,255])
    lower_red = np.array([110,100,100])
    mask = cv2.inRange(frame, lower_red, upper_red)
    frame = cv2.bitwise_and(frame,frame, mask=mask)    
    cv2.imshow('Single Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        print(key)
        break
    elif key ==ord('x'):
        print ('you have letter x')
        break
    
cam.release()
cv2.destroyAllWindows()    
