import cv2 as cv

img = cv.imread("./Resources/Photos/cats.jpg")
cv.imshow("cats", img)

# averaging
average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur , More effective than others in noise reduction
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

# Bilateral, the most effective, apply blurring but retains the edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)