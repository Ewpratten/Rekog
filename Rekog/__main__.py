from ingest import Webcam
from extraction import Face2Rect, Faces2Sort

import cv2
print("Starting Rekog")

# get webcam
cam = Webcam(0)
# cam = Webcam("http://172.16.10.28:8080/video")

# extractors
rect_overlay = Face2Rect()
face_crop_join = Faces2Sort()

# camera loop
while True:
    ret, image = cam.getFrame()
    if not ret: continue
    
    ret, image = face_crop_join.feed(image)
    if ret: continue
    # print(image)
    if str(image) == "[]": continue
    

    # if not image: continue
    # print(image)
    

    cv2.imshow("Rekog", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break