import cv2 as cv
import requests
import imutils
import numpy as np
url = "http://192.168.1.2:8080/shot.jpg"
class Camera:
    def __init__(self):
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv.imdecode(img_arr, -1)
        img = imutils.resize(img, width=900, height=900)
        self.camera  = img



    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return ret,None
        else:
            return None

camera = Camera()
ret,frame = camera.get_frame()
if ret:
    cv.imshow("camera feed", frame)
    cv.waitKey(0)
    cv

