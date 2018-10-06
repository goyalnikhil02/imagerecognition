import cv2
import numpy as np

image1 = cv2.imread("group.jpg")
image2 = cv2.imread("group2.jpg")

difference = cv2.subtract(image1, image2)

## if difference coatain 1,it return TRUE,mean images have difference
result =  np.any(difference) #if difference is all zeros it will return False(or say if no difference in images)

if result == True:
    cv2.imwrite("result.jpg", difference)
    cv2.imshow("result.jpg", difference)
    #print(difference)
    print ('the images are different')
    key=cv2.waitKey(10)
    
else :
    print ('The images are the same')

cv2.destroyAllWindows()
