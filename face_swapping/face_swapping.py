import cv2 as cv2
import numpy as np
import json
import cv2


  
def extract_index_nparray(nparray):
    index = None
    for num in nparray[0]:
        index = num
        break
    return index 

   
def draw_triangles(img, triangles):
    triangles = np.array(triangles, dtype=np.int32)
    for t in triangles:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        cv2.line(img, pt1, pt2, (0, 0, 255), 2)
        cv2.line(img, pt2, pt3, (0, 0, 255), 2)
        cv2.line(img, pt1, pt3, (0, 0, 255), 2)
    cv2.imshow("Original Image ", img)
    k = cv2.waitKey(3000)



def get_landmarks(landmark_filename):
    f1 = open(landmark_filename, 'r')
    data = json.loads(f1.read())
    landmarks = data["point"]   
    f1.close()    
    return landmarks
    


def triangle(landmarks, imshow=True):
    rec_of_point = bounding(landmarks)
    subdiv = cv2.Subdiv2D(rec_of_point)
    subdiv.insert(landmarks)
    triangles = subdiv.getTriangleList() 
    triangles = np.array(triangles, np.int32)    
    return triangles


def find_index_landmak(triangles, landmarks):
    triangles = np.array(triangles, np.int32)    
    landmarks = np.array(landmarks, np.int32)
    indexes_triangles = []
    for t in triangles:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        index_pt1 = np.where((landmarks == pt1).all(axis=1))
        index_pt1 = extract_index_nparray(index_pt1)
        index_pt2 = np.where((landmarks == pt2).all(axis=1))
        index_pt2 = extract_index_nparray(index_pt2)
        index_pt3 = np.where((landmarks == pt3).all(axis=1))
        index_pt3 = extract_index_nparray(index_pt3)
        if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
            triangle = [index_pt1, index_pt2, index_pt3]
            indexes_triangles.append(triangle)
    return indexes_triangles
  

def triangle2(indexes_triangles, landmarks, img2):
    triangles = []
    
    for triangle_index in indexes_triangles:
        pt1 = landmarks[triangle_index[0]]
        pt2 = landmarks[triangle_index[1]]
        pt3 = landmarks[triangle_index[2]]
        triangle = [pt1[0], pt1[1] ,pt2[0], pt2[1],pt3[0], pt3[1]]
        triangles.append(triangle)
    
    triangles = np.array(triangles)

    return triangles
       

def bounding(points):
    x_min = 999
    x_max = -999
    y_min = 999
    y_max = -999
    for x, y in points:
        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x   
        if y > y_max:
            y_max = y
        if y < y_min:
            y_min = y     
    rec_of_point = (x_min , y_min, x_max, y_max)
    return rec_of_point
    
    
        
 
def warp(img0, json_0, img1, json_1):
    landmarks_face1 = get_landmarks(json_0)
    landmarks_face2 = get_landmarks(json_1)
    points_landmarks = np.array(landmarks_face1, np.int32)
    new_face = np.zeros_like(img1)   
    triangle_face1 = triangle(landmarks_face1)
    indexes_triangles = find_index_landmak(triangle_face1, landmarks_face1)
     
    for triangle_index in indexes_triangles:
        
        tr1_pt1 = landmarks_face1[triangle_index[0]]
        tr1_pt2 = landmarks_face1[triangle_index[1]]
        tr1_pt3 = landmarks_face1[triangle_index[2]]
        triangle1 = np.array([tr1_pt1, tr1_pt2, tr1_pt3], np.int32)
        cropped_triangle1, points, rect1 = creat_mask(triangle1, img0)
        
        # cv2.line(img0, tr1_pt1, tr1_pt2, (0, 0, 255), 2)
        # cv2.line(img0, tr1_pt3, tr1_pt2, (0, 0, 255), 2)
        # cv2.line(img0, tr1_pt1, tr1_pt3, (0, 0, 255), 2)
        
     
        tr2_pt1 = landmarks_face2[triangle_index[0]]
        tr2_pt2 = landmarks_face2[triangle_index[1]]
        tr2_pt3 = landmarks_face2[triangle_index[2]]
        triangle2 = np.array([tr2_pt1, tr2_pt2, tr2_pt3], np.int32)
        cropped_triangle2, points2, rect2 = creat_mask(triangle2, img1)
        (x1, y1, x2, y2) = rect2
        
        # cv2.line(img1, tr2_pt1, tr2_pt2, (0, 0, 255), 2)
        # cv2.line(img1, tr2_pt3, tr2_pt2, (0, 0, 255), 2)
        # cv2.line(img1, tr2_pt1, tr2_pt3, (0, 0, 255), 2)
        
        points = np.float32(points)
        points2 = np.float32(points2)
        
        M = cv2.getAffineTransform(points, points2)
        warped = cv2.warpAffine(cropped_triangle1, M, (x2 - x1, y2 - y1))
          
        triangle_area = new_face[y1: y2, x1: x2]
        triangle_area = cv2.add(triangle_area, warped)
        new_face[y1: y2, x1: x2] = triangle_area
        
    
    new_face_gray = cv2.cvtColor(new_face, cv2.COLOR_BGR2GRAY)
    _, background = cv2.threshold(new_face_gray, 1, 255, cv2.THRESH_BINARY_INV)
    
    background = cv2.bitwise_and(img1, img1, mask=background)
    result = cv2.add(background, new_face)
     
    cv2.imshow("Img", img0)
    cv2.imshow("img2", img1)
    cv2.imshow("result", result)

    cv2.waitKey()
    cv2.destroyAllWindows()
    


def creat_mask(triangles, img):  
    rect1 = bounding(triangles)
    (x, y, x2, y2) = rect1
    
    cropped_triangle = img[y: y2, x: x2]
    cropped_tr1_mask = np.zeros((y2 - y, x2 - x), np.uint8)
    points = np.array([[triangles[0][0] - x, triangles[0][1] - y],
                      [triangles[1][0] - x, triangles[1][1] - y],
                      [triangles[2][0] - x, triangles[2][1] - y]], np.int32)
    cv2.fillConvexPoly(cropped_tr1_mask, points, 255)
    cropped_triangle = cv2.bitwise_and(cropped_triangle, cropped_triangle,
                                       mask=cropped_tr1_mask)
    
    return cropped_triangle, points, rect1



if __name__ == '__main__':
    json_0 = 'Im387.json'
    json_1 = 'Im386.json'
    image0_path = 'Im387_resize_.png'
    image1_path = 'Im386_resize_.png'
    img0 = cv2.imread(image0_path)
    img1 = cv2.imread(image1_path)
    
    warp(img0, json_0, img1, json_1)
    
