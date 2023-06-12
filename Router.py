from tkinter import *


class Router:

    def __init__(self, name):
        self.image = PhotoImage(file="img/router.png")
        self.image_red = PhotoImage(file="img/router_red.png")
        self.image_green = PhotoImage(file="img/router_green.png")
        self.name = name
        self.ports = [["None", "None"] for i in range(2)]
        self.x = None
        self.y = None
        self.canvas_img = None
        self.mac = None

    def highlight_router(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image_green)

    def unhighlight_router(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image)

    def edit_device(self, port, device, address):
        self.ports[port - 1][0] = device.name
        self.ports[port - 1][1] = device
        self.mac = address

    def place_router(self, cnvs, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.canvas_img = cnvs.create_image((self.x, self.y), image=self.image)

    def port(self, n):
        if n == 1:
            return self.x - 50
        elif n == 2:
            return self.x + 50
