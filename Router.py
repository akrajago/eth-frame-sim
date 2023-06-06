from tkinter import *


class Router:

    def __init__(self, name):
        self.image = PhotoImage(file="img/router.png")
        self.pic_label = Label(image=self.image)
        self.name = name
        self.ports = ["None", "None"]
        self.x = None
        self.y = None
        self.canvas_img = None

    def highlight_device(self, event):
        self.pic_label.configure(bg="pink")

    def unhighlight_device(self, event):
        self.pic_label.configure(bg="white")

    def place_router(self, cnvs, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.canvas_img = cnvs.create_image((self.x, self.y), image=self.image)
        # self.pic_label.place(x=x_coord, y=y_coord)
