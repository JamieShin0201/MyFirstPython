import cv2


image1 = cv2.imread("puppy1.png", cv2.IMREAD_COLOR)
image2 = cv2.imread("puppy2.png", cv2.IMREAD_COLOR)

result = cv2.add(image1[0:150, 0:150], image2[0:150, 0:150])
cv2.imshow("Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows();

result = image1[0:150, 0:150] + image2[0:150, 0:150]
cv2.imshow("Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows();

# 이미지 합치기
# cv2.add : Saturation 연산 (255가 넘어가면 255)
# 주로 cv2.add 사용
# np.add() : Modulo 연산 (255 넘어가면 0부터 다시시작)


