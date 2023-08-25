import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("./Resources/Photos/hist_ex.png", 0)
cv.imshow("Low contrast image", img)

# plot histogram
histogram = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histogram, color='k')
plt.show()

# histogram equalization
out_img = cv.equalizeHist(img)
cv.imshow("High contrast image", out_img)

# CLAHE
clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(11,11))
out_image = clahe.apply(img)
cv.imshow("CLAHE", out_image)

# RGB histogram equalization
img_rgb= cv.imread("./Resources/Photos/group 2.jpg")
cv.imshow("RGB image", img_rgb)

img_hsv = cv.cvtColor(img_rgb, cv.COLOR_BGR2HSV)
h, s, v = cv.split(img_hsv)
v_new = cv.equalizeHist(v)
new_image = cv.cvtColor(cv.merge((h, s, v_new)), cv.COLOR_HSV2BGR)
cv.imshow("RGB histogram equalization", new_image)


cv.waitKey(0)