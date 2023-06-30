import cv2

class Camera:
    def __init__(self):
        self.camera  = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Camera not Found!")

