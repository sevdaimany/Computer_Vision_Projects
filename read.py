import cv2 as cv



# reading an image
img = cv.imread("Resources/Photos/cat.jpg")

cv.imshow("cat", img)

cv.waitKey(0)

# reading a video

capture = cv.VideoCapture("Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        cv.imshow("Dog", frame)
        if cv.waitKey(20) & 0xff==ord("d"):
            break
    else:
        break

