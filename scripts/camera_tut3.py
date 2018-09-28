import cv2
import numpy as np
cam = cv2.VideoCapture(0)
#print(cam.get(cv2.CAP_PROP_FRAME_WIDTH ))

tf, frame = cam.read()
cv2.imshow("Single Frame",frame)

#capture the frmae and save as image
cv2.imwrite("grey_camera.jpg", frame)

cv2.waitKey(10)
cam.release()
cv2.destroyAllWindows()
