from tkinter.tix import PopupMenu
import cv2
import numpy as np
import json

# Create point matrix get coordinates of mouse click on image
counter = 0 
num_point = 5
point_matrix = np.zeros((num_point,2),np.int)

def mousePoints(event, x, y, flags, params):
    global counter
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        
        point_matrix[counter] = int(x), int(y)
        counter = counter + 1


img = cv2.imread("D:\\part_college\\part_2\\Untitled Folder\\face_ramin_rahimi\\face_ramin_rahimi\\images\\Im387.bmp")
img = cv2.resize(img, dsize=(500, 600))
cv2.imwrite('Im387_resize_.png', img)

while True:
    # show circle of points

    if counter == num_point:
        # point_matrix = [[int(x), int(y)] for item in  ...]
        for i in range(num_point):
            cv2.circle(img, (point_matrix[i][0],point_matrix[i][1]), 3, (0, 255,0), -1)
        # cv2.imshow("obama",img)
        with open("Dataset.json", "w") as f:
            lists = point_matrix.tolist()
            json_str = json.dumps(lists)
        counter +=1



    # Showing original image
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    k = cv2.waitKey(300)
