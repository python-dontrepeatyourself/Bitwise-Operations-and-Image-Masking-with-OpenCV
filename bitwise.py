import cv2
import numpy as np


# draw a horizontal rectangle
image1 = np.zeros((400, 600), dtype="uint8")
cv2.rectangle(image1, (50, 50), (250, 350), 255, -1)

# draw a vertical rectangle
image2 = np.zeros((400, 600), dtype="uint8")
cv2.rectangle(image2, (50, 200), (550, 350), 255, -1)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)

# bitwise AND
bitwise_and = cv2.bitwise_and(image1, image2)
cv2.imshow("bitwise_and", bitwise_and)
cv2.waitKey(0)

# bitwise OR
bitwise_or = cv2.bitwise_or(image1, image2)
cv2.imshow("bitwise_or", bitwise_or)
cv2.waitKey(0)

# bitwise XOR
bitwise_xor = cv2.bitwise_xor(image1, image2)
cv2.imshow("bitwise_xor", bitwise_xor)
cv2.waitKey(0)

# bitwise NOT
bitwise_not = cv2.bitwise_not(image1)
cv2.imshow("bitwise_not image1", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()


