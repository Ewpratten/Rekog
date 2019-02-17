import cv2
import numpy as np

class Face2Rect(object):
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("./classifiers/harr")

    def feed(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        return frame

class Faces2Sort(object):
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("./classifiers/harr")

    def feed(self, frame):
        output = []

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        # print(faces)
        if str(faces) == "()":
            return 1, None
            
        for (x, y, w, h) in faces:
            output.append( frame[y:y+h, x:x+w])
            return 0,frame[y:y+h, x:x+w]
        
        
        return 0,np.concatenate(tuple(output), axis=1)