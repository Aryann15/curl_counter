import tkinter as tk
import os
import PIL.Image, PIL.ImageTk
import cv2
import camera


class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Curl Counter"

        self.counters = [1, 1]
        self.rep_counter = 0

        self.extended = False
        self.contracted = False

        self.last_prediction = 0

        self.counting_enabled = False

        self.camera = camera.Camera()


