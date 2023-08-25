# Contours are defined as the line joining all the points along the boundary 
# of an image that are having the same intensity. Contours come handy in
# shape analysis, finding the size of the object of interest, and object detection.

# Contour is the edge closing an object. So you can think as higher level of edge detection.

# So if an edge define an object it becomes a contour.
import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow("cat", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny Edges", canny)


# # instead of blur and canny we can use threshold, it binarilize the image
# but first check the canny
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0 ,0 , 255), 2)
cv.imshow("Contours Drawn", blank)


cv.waitKey(0)
