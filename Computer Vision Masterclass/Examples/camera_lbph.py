import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("lbph_classifier.yml")
width, height = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while (True):
    connected, image = camera.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(image_gray, scaleFactor=1.5, minSize=(30,30))
    for (x, y, w, h) in detections:
        image_face = cv2.resize(image_gray[y:y + w, x:x + h], (width, height))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2)
        id, confidence = face_recognizer.predict(image_face)
        name = ""
        if id == 1:
            name = 'Jones'
        elif id == 2:
            name = 'Gabriel'
        cv2.putText(image, name, (x,y +(w+30)), font, 2, (0,0,255))
        cv2.putText(image, str(confidence), (x,y + (h+50)), font, 1, (0,0,255))

    cv2.imshow("Face", image)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()