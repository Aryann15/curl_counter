import cv2

class Camera:
    def __init__(self):
        self.camera  = cv2.VideoCapture(0)
