import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/cat.jpg", 0)
cv.imshow("image", img)

def gamma_correction(img, gamma=0.5):
    map_gray = np.array([((i/255)**gamma)*255 for i in range(256)]).astype(np.uint8)
    image_out = cv.LUT(img, map_gray)
    return image_out


img_out = gamma_correction(img, .5)
cv.imshow("gamma correction", img_out)


cv.waitKey(0)