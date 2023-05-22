from tkinter import *

class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.name = name
        self.ports = []

    def add_device(self, port, d_type, name):
        self.ports[port] = name
