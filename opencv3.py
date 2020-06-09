import cv2
import numpy as np

image = cv2.imread("puppy1.png", cv2.IMREAD_COLOR)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows();

# 이미지 크기 조절
expend = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Image", expend)
cv2.waitKey(0)
cv2.destroyAllWindows();

shrink = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("Image", shrink)
cv2.waitKey(0)
cv2.destroyAllWindows();

# 이미지 위치 변형
image = cv2.imread("puppy1.png", cv2.IMREAD_COLOR)
height, width = image.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 100]])
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows();

# 이미지 회전

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows();

print(M)

