from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.pic_label = Label(image=self.image)
        self.name = name
        self.ports = [["None", "None", "None"] for i in range(4)]
        self.x = None
        self.y = None
        self.canvas_img = None

    def highlight_device(self, event):
        self.pic_label.configure(bg="pink")

    def unhighlight_device(self, event):
        self.pic_label.configure(bg="white")

    def edit_device(self, port, dev_type, name):
        self.ports[port - 1][0] = name
        print(dev_type)

    def remove_device(self, frame, port):
        self.ports[port - 1] = ["None", "None"]

    def place_switch(self, cnvs, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.canvas_img = cnvs.create_image((self.x, self.y), image=self.image)

    def port(self, n):
        if int(n) == 1:
            return self.x - 147
        elif int(n) == 2:
            return self.x - 60
        elif int(n) == 3:
            return self.x + 30
        elif int(n) == 4:
            return self.x + 117


