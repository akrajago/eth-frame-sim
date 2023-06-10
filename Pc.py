from tkinter import *


class Pc:

    def __init__(self, name):
        self.image = PhotoImage(file="img/pc.png")
        self.name = name
        self.x = None
        self.y = None
        self.canvas_img = None
        self.switch = None

    def edit_device(self, switch):
        self.switch = switch

    def place_pc(self, cnvs, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.canvas_img = cnvs.create_image((self.x, self.y), image=self.image)
