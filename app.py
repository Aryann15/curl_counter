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

        self.model = None

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

        self.btn_toggleauto = tk.Button(self.window, width=50, text= "Toggle Counting", command=self.counting_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER , expand=True)

        self.btn_class_one = tk.Button(self.window, width=50,  text="Extended arms", command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, width=50, text="Contracted arms", command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, width=50, text="Start Training!",command=lambda: self.model.train_model(self.counters))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = tk.Button(self.window, width=50, text="Reset",command=self.reset)
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.counter_label = tk.Label(self.window,  text= f"{self.rep_counter}")
        self.counter_label.config(font=("Arial",24))
        self.counter_label.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        pass

    def predict(self):
        pass

    def counting_toggle(self):
        self.counting_enabled = not self.counting_enabled

    def save_for_class(self, class_num):
        ret, frame= self.camera.get_frame()
        if not os.path.exists("1"):
            os.mkdir("1")
        if not os.path.exists("2"):
            os.mkdir("2")

        cv2.imwrite(f'{class_num}/frame{self.counters[class_num-1]}.jpg', cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
        img = PIL.Image.open(f'{class_num}/frame{self.counters[class_num-1]}.jpg')
        img.thumbnail ((150,150), PIL.Image.ANTIALIAS)
        img.save(f'{class_num}/frame{self.counters[class_num-1]}.jpg')
        self.counters[class_num-1] +=1

    def reset(self):
        self.rep_counter= 0