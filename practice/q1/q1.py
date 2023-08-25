import cv2 as cv
import numpy as np


video = cv.VideoCapture('./bmw-m5-f10_crop2.mp4')
frame_rate = video.get(5)
frame_size = np.int64((video.get(3), video.get(4)))
output = cv.VideoWriter('speed.avi', cv.VideoWriter_fourcc('M','J','P','G'), frame_rate, frame_size)

while True:
    ok, frame = video.read()
    if not ok:
        break
    
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(img_gray, 150, 255)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 60, minLineLength=30, maxLineGap=3)
    img_hough_linesP = frame.copy()
    if not (lines is None):
        
        for line in lines:
            x1, y1, x2, y2 = line[0]
            mag = np.sqrt((x2 - x1)**2 + (y2 - y1) **2)
            angel = -(180/np.pi)*np.arctan((y2 - y1)/ (x2 - x1 + np.finfo(float).eps))
            
            if  min(x1,x2) < 72 or angel < 0:
                angel += 180
                
        cv.line(img_hough_linesP, (x1, y1), (x2,y2), (0,0,255), 2)
        speed = -1.4*angel+289
        cv.putText(img_hough_linesP, str(int(angel)) , (80, 150), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 255), 2)
        print(mag, angel, x1, x2)
       
            
        output.write(img_hough_linesP)
        cv.imshow("speed" , img_hough_linesP)
        
        if cv.waitKey(1) & 0XFF == 27: #esc
            break

    
            
            
output.release()
video.release()