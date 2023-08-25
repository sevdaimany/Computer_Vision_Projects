# Erosion, Dilation, Opening, Closing
import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/ex_mor.png")
if img is None:
    print("There is no image!")
cv.imshow("image", img)
   
# EROSION
str_el = np.ones((9, 9)).astype(np.uint8)
image_erosion = cv.erode(img, str_el)
cv.imshow("Erosion", image_erosion) 

# it doesn't work in this way: cv.erode(img, (9, 9)). WHY?
# DILATION
str_el = np.ones((9,9)).astype(np.uint8)
image_dilation = cv.dilate(img, str_el)
cv.imshow("Dilation", image_dilation)
image_border_dilate = np.subtract(image_dilation, img)
cv.imshow("border dilation", image_border_dilate)

# 

# OPENING
img = cv.imread("./Resources/Photos/opening_noise.png")
if img is None:
    print("There is no image!")
cv.imshow("opening image", img)

str_el = np.ones((5,5)).astype(np.uint8)
out_image = cv.morphologyEx(img,cv.MORPH_OPEN,str_el)
cv.imshow("opening image denoised", out_image)



# CLOSIMG
img = cv.imread("./Resources/Photos/closing_noise.png")
if img is None:
    print("There is no image!")
cv.imshow("closing image", img)

str_el = np.ones((5,5)).astype(np.uint8)
out_image = cv.morphologyEx(img,cv.MORPH_CLOSE,str_el)
cv.imshow("closing image denoised", out_image)

# Extracting vertical lines
img = cv.imread("./Resources/Photos/line_mor.png")
if img is None:
    print("There is no image!")
cv.imshow("lines", img)

str_el = np.ones((11,1)).astype(np.uint8)
out_image = cv.morphologyEx(img,cv.MORPH_OPEN,str_el)
cv.imshow("vertical lines", out_image)




cv.waitKey(0)

