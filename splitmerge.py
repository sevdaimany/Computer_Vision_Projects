import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/park.jpg")
cv.imshow("park", img)


b, g, r = cv.split(img)
cv.imshow("Blue", b)
cv.imshow("green", g)
cv.imshow("red", r)


print(img.shape)
print(b.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)



cv.waitKey(0)