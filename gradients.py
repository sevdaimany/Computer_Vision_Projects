# Canny, Laplacian, Sobel
import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/park.jpg")
# cv.imshow("park", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8 (np.absolute(lap))
cv.imshow("Laplacian", lap)

# sobel, compute the gradients in two directions, x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel x", sobelx)
cv.imshow("Sobel y", sobely)
cv.imshow("combined Sobel", combined_sobel)

# sobel
img2 = cv.imread("./Resources/Photos/Arrow.jpg", 0)
cv.imshow("Arrow", img2)
sobelx = cv.Sobel(img2, cv.CV_16S, 1, 0)
sobely = cv.Sobel(img2, cv.CV_16S, 0, 1)
sobelx_np = cv.convertScaleAbs(sobelx)
sobely_np = cv.convertScaleAbs(sobely)
cv.imshow("Sobel x Arrow", sobelx_np)
cv.imshow("Sobel y Arrow", sobely_np)


# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)



cv.waitKey(0)