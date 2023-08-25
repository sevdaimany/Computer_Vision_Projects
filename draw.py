import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype="uint8")
# paint the whole image green
blank[:] = 0, 255, 0
cv.imshow("blank", blank)

# draw a rectangle
# cv.rectangle(blank, (0,0), (300, 300), (0, 100, 100), thickness=3)
cv.rectangle(blank, (0,0), (300, 300), (0, 100, 100), thickness=cv.FILLED)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# put a text 
cv.putText(blank, "Hello everybody", (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("blank", blank)


img = cv.imread("./Resources/Photos/cat.jpg")
cv.imshow("Cat", img)
cv.waitKey(0)