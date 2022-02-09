# Computer Vision
Some simple computer vision implementations using OpenCV.

## Object Detection
In this project, I build an object detection system. The system consists 
of a face detector and object detector that uses Haar Cascades, a 
Convolutional Neural Network (CNN), and Histograms of Oriented Gradients 
(HOG) that predict the faces and objects like cars, clocks, and full 
body.

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/screenshots/face_detection.png)



## Face Recognition
Using OpenCV and dlib inbuilt functions to recognize faces. The code uses  Dlib frontal face 
detector to identify facial features. LBPH Face Recognizer is used to recognize differences 
between faces. LBPH (Local Binary Patterns Histogram) algorithm is used to identify faces.
and dlib face recognition resnet model v1 is used to recognize differences between faces with 
higher accuracy than LBPH algorithm.

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/screenshots/face_recognition_1.png)

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/screenshots/face_recognition_2.png)


## Object Tracking

Implementing object tracker using KCF and CSRT trackers from OpenCV.
Amongst all the tracking methods available KCF and CSRT are the most accurate considering all 
the pros and cons. KCF is very fast when it comes to processing the video while the CSRT is a 
bit slow but the tracking of the object is precise.


![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/screenshots/object_tracking.png)



## Face Swapping

In this project, first, the landmarks of both faces are given by the user, so that from them we can find the external boundaries of the face. Be careful that the order of landmarks in both faces should 
be the same. Then save landmark points in a JSON file.
In the second part, split the face into triangles using Delaunay Triangulation.
split both the faces into triangles and then we swap the triangles in the correspondent region.

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/face_swapping/Screenshot2.png)

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/face_swapping/Screenshot1.png)

![github-octocat](https://github.com/sevdaimany/Computer_Vision_Projects/blob/master/face_swapping/result.png)





### Install

This project files requires **Python 3** and the following Python 
libraries installed:

- [OpenCV](https://opencv.org/)
- [Numpy](http://numpy.org/)
- [dlib](https://github.com/davisking/dlib)

Following are some links to install OpenCV and dlib on mac, windows and 
linux:


[OpenCV](https://github.com/opencv/opencv) - 
[Mac](https://www.learnopencv.com/install-opencv3-on-macos/) | 
[Windows](https://www.learnopencv.com/install-opencv3-on-windows/) | 
[Ubuntu](https://www.learnopencv.com/install-opencv3-on-ubuntu/)


[Dlib](https://github.com/davisking/dlib) -   
[Mac](https://www.learnopencv.com/install-dlib-on-macos/) | 
[Windows](https://www.learnopencv.com/install-dlib-on-windows/) | 
[Ubuntu](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/)
