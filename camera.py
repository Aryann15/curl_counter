import cv2

class Camera:
    def __init__(self):
        self.camera  = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Camera not Found!")

        self.width =self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height =self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return ret,
            else:
                return ret,None
        else:
            return None