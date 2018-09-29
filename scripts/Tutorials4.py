import cv2
import numpy as np


#flags = [color for color in dir(cv2) if color.startswith('COLOR_')]
#print (flags)

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output.avi', fourcc, 6, (640,480))

while(True):
    tf,frame = cam.read()
    #print(tf)
    ## to change the video framwe in grey color
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    video.write(frame)
    cv2.imshow('Single Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        print(key)
        break
    elif key ==ord('x'):
        print ('you have letter x')
        break
cam.release()    
video.release()
cv2.destroyAllWindows()    
