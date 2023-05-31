from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.name = name
        self.ports = [None] * 4

    def add_device(self, port, name):
        self.ports[port - 1] = name
