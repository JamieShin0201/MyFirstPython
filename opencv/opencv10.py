import cv2
import numpy as np

image = cv2.imread("../images/puppy1.png")
cv2.imshow("Image", image)
cv2.waitKey(0)

size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

dst = cv2.filter2D(image, -1, kernel)
cv2.imshow("Image", dst)
cv2.waitKey(0)

image = cv2.imread("../images/puppy1.png")
cv2.imshow("Image", image)
cv2.waitKey(0)

dst = cv2.blur(image, (4, 4))
cv2.imshow("Image", dst)
cv2.waitKey(0)

image = cv2.imread("../images/puppy1.png")
cv2.imshow("Image", image)
cv2.waitKey(0)

# kernel_size: 홀수
dst = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", dst)
cv2.waitKey(0)