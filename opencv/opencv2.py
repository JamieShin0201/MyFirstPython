import cv2
import time

# opencv 이미지 연산
image = cv2.imread("../images/puppy1.png", cv2.IMREAD_COLOR)

print(image.shape)
print(image.size)

px = image[100, 100]
print(px)

print(px[2])

# px = image[500, 100]
# out of bound

# 특정 범위 픽셀 변경
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows();

# 빠른 연산 가능
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows();

# ROI 추출 및 복사 (Region Of Interest)
image = cv2.imread("../images/puppy1.png", cv2.IMREAD_COLOR)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows();

logo = image[20:150, 70:200]
cv2.imshow("Image", logo)
cv2.waitKey(0)
cv2.destroyAllWindows();

# ROI 단위로 이미지 복사
image[0:130, 0:130] = logo
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows();

# 픽셀별로 색상 다루기
image = cv2.imread("../images/puppy1.png", cv2.IMREAD_COLOR)
# B G R (0 1 2)
cv2.imshow("Image", image[:, :, 2])
cv2.waitKey(0)

image[:, :, 2] = 0;
cv2.imshow("Image", image)
cv2.waitKey(0)

