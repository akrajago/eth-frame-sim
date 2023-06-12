from tkinter import *


class Pc:

    def __init__(self, name):
        self.image = PhotoImage(file="img/pc.png")
        self.image_red = PhotoImage(file="img/pc_red.png")
        self.image_green = PhotoImage(file="img/pc_green.png")
        self.name = name
        self.x = None
        self.y = None
        self.canvas_img = None
        self.switch = None
        self.mac = None
        self.port = None

    def highlight_pc(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image_green)

    def unhighlight_pc(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image)

    def set_info(self, port, address):
        self.port = port
        self.mac = address

    def place_pc(self, cnvs, switch, x_coord, y_coord):
        self.switch = switch
        self.x = x_coord
        self.y = y_coord
        self.canvas_img = cnvs.create_image((self.x, self.y), image=self.image)

