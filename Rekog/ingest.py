import cv2

class Webcam(object):
    def __init__(self, cam_id=0):
        self.cam = cv2.VideoCapture(cam_id)
    
    def getFrame(self):
        return self.cam.read()