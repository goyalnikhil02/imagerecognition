import cv2
import numpy as np

im = cv2.imread('C:\\Users\\g521784\\Desktop\\ImageRecognistation\\images\\nikhil.jpeg')
im1 = cv2.imread('C:\\Users\\g521784\\Desktop\\ImageRecognistation\\images\\b.jpg')
kernel = np.ones((5,5), np.uint8) 
print (im)
print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
print (im1)


img_erosion = cv2.dilate(im, kernel, iterations=1)

#grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('firstimg',grayA)

#grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#cv2.imshow('secondimg',grayB)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
#diff = cv2.subtract(img2, img1)

cv2.imwrite("c:\\see_this.jpg", img_erosion)

diff = cv2.subtract(img_erosion, im)


print(diff)


