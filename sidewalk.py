import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('146.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)

boundaries = [
	([132, 103, 40], [255, 255, 255])
]

for (lower, upper) in boundaries:

	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors
	mask = cv2.inRange(blur, lower, upper)
	output = cv2.bitwise_and(blur, blur, mask = mask)
 

blur = cv2.GaussianBlur(output,(5,5),0)
edges = cv2.Canny(blur,100,200)
    
# show the images
cv2.imshow("mask", output)
cv2.imshow("edges", edges)
cv2.imshow("image", img)
cv2.waitKey(0)
