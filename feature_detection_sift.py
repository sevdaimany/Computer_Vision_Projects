import cv2 as cv

image = cv.imread("./Resources/Photos/cat.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# SIFT
img = image.copy()
des = cv.SIFT_create()
kpt, feature = des.detectAndCompute(img, None)
image_out = cv.drawKeypoints(img, kpt, None, [255,0,0])
cv.imshow("SIFT", image_out)

# ORB
img = image.copy()
des = cv.ORB_create()
kpt, feature = des.detectAndCompute(img, None)
image_out = cv.drawKeypoints(img, kpt, None, [255,0,0])
cv.imshow("ORB", image_out)

# BRISK
img = image.copy()
des = cv.BRISK_create()
kpt, feature = des.detectAndCompute(img, None)
image_out = cv.drawKeypoints(img, kpt, None, [255,0,0])
cv.imshow("BRISK", image_out)

# SURF
# Applying the function
img = image.copy()
fast = cv.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)
# Drawing the keypoints
kp = fast.detect(img, None)
kp_image = cv.drawKeypoints(img, kp, None, color=(0, 255, 0))
cv.imshow('FAST', kp_image)

cv.waitKey(0)