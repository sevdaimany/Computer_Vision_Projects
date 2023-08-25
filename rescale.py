import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    # for image, video and live video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimention = (width, height)
    
    return cv.resize(frame, dimention, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # for live video
    # 3 refrences width and 4 refrences height
    capture.set(3, width)
    capture.set(4, height)
    
img = cv.imread("Resources/Photos/cat_large.jpg")
# cv.imshow("cat", img)
# cv.waitKey(0)

img_resized = rescaleFrame(img)
cv.imshow("cat", img_resized)
# cv.waitKey(0)

capture = cv.VideoCapture("Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        resized_frame = rescaleFrame(frame)
        cv.imshow("dog", resized_frame)
        if cv.waitKey(20) & 0xff==ord('d'):
            break
    else:
        break
    
capture.release()
cv.destroyAllWindows()
    