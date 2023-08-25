import cv2 as cv
import numpy as np

video = cv.VideoCapture("./dumbbell.mp4")
frame_rate = video.get(5)
frame_size = np.int64((video.get(3), video.get(4)))
