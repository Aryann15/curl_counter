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
        self.camera  = cv.cvtColor(img,cv.COLOR_BGR2RGB)



    def __del__(self):
        pass

    def get_frame(self):
        return True, self.camera

camera = Camera()
ret,frame = camera.get_frame()
if ret:
    cv.imshow("camera feed", frame)
    cv.waitKey(0)
    cv

