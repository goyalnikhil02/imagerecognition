import  numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
vid = cv2.VideoWriter('capturing_screen.avi', fourcc, 8, (600,500))
while(True):
    img_np = np.array(ImageGrab.grab(bbox=(0, 0, 600, 500))) #x, y, w, h
    vid.write(img_np)
    cv2.imshow("frame", img_np)
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        print(key)
        break    

vid.release()
cv2.destroyAllWindows()