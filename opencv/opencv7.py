import cv2
import numpy as np

# OpenCV 도형 그리기

# 직선그리기
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 10)
cv2.imshow("Image", image)
cv2.waitKey(0)

# 사각형 그리기
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), -1)
cv2.imshow("Image", image)
cv2.waitKey(0)

# 원 그리기
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255, 255), 30, (255, 0, 0), -1)
cv2.imshow("Image", image)
cv2.waitKey(0)

# 다각형 그리기
image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (255, 0, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)

# 텍스트 그리기
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, "Hello World", (0, 200), cv2.FONT_ITALIC, 1, (255, 0, 0))
cv2.imshow("Image", image)
cv2.waitKey(0)

