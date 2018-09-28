import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\g521784\\Desktop\\ImageRecognistation\\images\\nikhil.jpeg')

print (img1)

grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('firstimg',grayA)
cv2.imwrite("grey_this.jpg", grayA)
