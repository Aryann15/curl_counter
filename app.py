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

        self.init_gui()

        self.delay=15
        self.update()

        self.window.attributes("-topmost",True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(self.window,width=self.camera.width,height=self.camera.height)
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text= "Toggle Counting", command=self.counting_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER , expand=True)


    def counting_toggle():
        pass

