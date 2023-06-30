import cv2
import PIL
import numpy as np
from sklearn.svm import LinearSVC

class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self,counters):
        img_list = np.array([])
        class_list = np.array([])

