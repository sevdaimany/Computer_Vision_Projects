import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/PartLogo.png")
cv.imshow("image", img)

# Harris corner detection
img_harris = img.copy()
img_gray = cv.cvtColor(img_harris, cv.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
corners = cv.cornerHarris(img_gray, 2, 3, 0.04)
corners = cv.dilate(corners, None)
img_harris[corners > 0.1 * corners.max()] = [0, 0, 255]
cv.imshow("corners Harris", img_harris)

# shi- tomasi corner detection
img_tomasi = img.copy()
img_gray = cv.cvtColor(img_tomasi, cv.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
corners = cv.cornerMinEigenVal(img_gray, 2, 3)
corners = cv.dilate(corners, None)
img_tomasi[corners > 0.1 * corners.max()] = [0, 0, 255]
cv.imshow("corners Tomasi", img_tomasi)

# goodfeaturestotrack - usually use in optical flow
img_corner = img.copy()
img_gray = cv.cvtColor(img, 6)
img_gray = np.float32(img_gray)
corners = cv.goodFeaturesToTrack(img_gray, 10, 0.01, 10)
corners = np.int0(corners)
print(corners)
for corner in corners:
    cv.circle(img_corner, corner[0],1, (0,0,255), 3, -1)

cv.imshow("good to track", img_corner)


cv.waitKey(0)