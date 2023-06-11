from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.name = name
        self.ports = [["None", "None", "None"] for i in range(4)]
        self.x = None
        self.y = None
        self.canvas_img = None
        self.mac_table = {}

    def add_mac_entry(self, address, port):
        self.mac_table[address] = port

    def edit_device(self, port, dev_type, device):
        self.ports[port - 1][0] = device.name
        self.ports[port - 1][1] = device.mac
        print(dev_type)

    def remove_device(self, frame, port):
        self.ports[port - 1] = ["None", "None", "None"]

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


