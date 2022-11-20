import cv2
import numpy as np


moon = cv2.imread("bitwise-operations/moon.jpg")

# create a black image with the same size as our 
# image that contains the moon, we then create
# a white circle on the black image
mask = np.zeros(moon.shape[:2], dtype="uint8")
cv2.circle(mask, (202, 133), 34, 255, -1)

# apply the mask to our image
masked = cv2.bitwise_and(moon, moon, mask=mask)

cv2.imshow("moon", moon)
cv2.imshow("mask", mask)
cv2.imshow("Mask applied to image", masked)
cv2.waitKey(0)
