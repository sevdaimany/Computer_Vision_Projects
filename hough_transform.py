import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/highway.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_canny = cv.Canny(img_gray, 100, 200)
# cv.imshow("concate",  np.concatenate((img_gray, img_canny), 1))

# Hough transform
lines = cv.HoughLines(img_canny, 1, np.pi/180, 60)
rho_max = np.sqrt(img.shape[0]**2+img.shape[1]**2)
img_hough_line = img.copy()
# print(lines)
for line in lines:
    rho = line[0][0]
    theta = line[0][1] 
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x0 = rho * cos_theta
    y0 = rho * sin_theta
    pts1 = (int(x0 - rho_max * sin_theta), int(y0 + rho_max * cos_theta))
    pts2 = (int(x0 + rho_max * sin_theta), int(y0 - rho_max * cos_theta))
    cv.line(img_hough_line, pts1, pts2, (0,0, 255), 2)

cv.imshow("highway lines", img_hough_line)

# the probabilistic Hough transform.
img_hough_linesP = img.copy()
lines = cv.HoughLinesP(img_canny, 1, np.pi/180, 40, minLineLength=100, maxLineGap=500)
print(lines)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img_hough_linesP, (x1, y1), (x2, y2), (0,0,255), 3)
cv.imshow("highway lines probabilistic", img_hough_linesP)

# Hough circle
img = cv.imread("./Resources/Photos/baby.jpg")
img_gray = cv.cvtColor(img, 6)
img_blur = cv.medianBlur(img_gray,5)
circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, dp=1, minDist=200, param1=50, param2=30, minRadius=50, maxRadius=90)
# print(circles)
circles = np.uint16((circles))
for circle in circles[0]:
    print(circle)
    cv.circle(img, (circle[0], circle[1]), circle[2], (0,0,255), 3)
    cv.circle(img, (circle[0], circle[1]), 10, (0,0,255), -1)

cv.imshow("baby", img)
cv.waitKey(0)