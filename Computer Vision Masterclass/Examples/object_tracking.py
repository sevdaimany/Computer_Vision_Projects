import cv2

#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('street.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)
#print(bbox)

ok = tracker.init(frame, bbox)
#print(ok)

while True:
    ok, frame = video.read()
    #print(ok)
    if not ok:
        break
    ok, bbox = tracker.update(frame)
    #print(bbox)
    #print(ok)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # ESC
        break

