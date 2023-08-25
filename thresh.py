# thresholding is a binarization of an image
# compare each pixel of the image with the threshold 
# if that pixel intensity is less than the threshold value, set the pixel intensity to zero
# and, if it is above, set it to 255, white
import cv2 as cv
import numpy as np
 

img = cv.imread("./Resources/Photos/cats.jpg")
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple thresholding

threshold, thresh = cv.threshold(gray,150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# adaptive thresholding, don't have to manually specify a specific threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresholding", adaptive_thresh )


# Green space detection using LAB color space 
img = cv.imread("./Resources/Photos/city.JPG")
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
l, a, b = cv.split(img_lab)
print(l.min(), a.min(), b.min())
print(l.max(), a.max(), b.max())

lbound = (0, 0, 150)
ubound = (255, 150, 255)
img_lab_green = cv.inRange(img_lab, lbound, ubound)
img_lab_green_resized = cv.resize(img_lab_green, (600,500), interpolation=cv.INTER_CUBIC)
cv.imshow('park', img_lab_green_resized)


# OTSU Thresholding
image  = cv.imread('./Resources/Photos/otsu.jpg',0)
cv.imshow("image OTSU", image)
thre,image_bin = cv.threshold(image,-1,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("OTSU", image_bin)
print(image_bin)


cv.waitKey(0)

