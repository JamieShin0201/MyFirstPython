import cv2

image = cv2.imread("../images/digit_image.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Image", thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)

contours = contours[2]
x, y, w, h = cv2.boundingRect(contours)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 10)
cv2.imshow("Image", image)
cv2.waitKey(0)


image = cv2.imread("../images/digit_image.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

contours = contours[2]
hull = cv2.convexHull(contours)
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)


image = cv2.imread("../images/digit_image.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

contour = contours[2]
epsilon = 0.01 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)


image = cv2.imread("../images/digit_image.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

contour = contours[2]
area = cv2.contourArea(contour)
print(area)
length = cv2.arcLength(contour, True)
print(length)
M = cv2.moments(contour)
print(M)





