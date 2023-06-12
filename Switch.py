from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.image_red = PhotoImage(file="img/switch_red.png")
        self.image_green = PhotoImage(file="img/switch_green.png")
        self.name = name
        self.ports = [["None", "None", "None"] for i in range(4)]
        self.timer = 10
        self.x = None
        self.y = None
        self.canvas_img = None
        self.mac = "None"
        self.mac_table = {}

    def highlight_switch(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image_green)

    def unhighlight_switch(self, cnvs):
        cnvs.itemconfigure(self.canvas_img, image=self.image)

    def add_mac_entry(self, cnvs, address, port):
        self.mac_table[address] = [port, self.timer]
        self.decrement_time(cnvs, address)

    def reset_timer(self, frame, address):
        self.mac_table[address][1] = self.timer
        self.decrement_time(frame, address)

    def decrement_time(self, frame, address):
        if self.mac_table[address][1]:
            self.mac_table[address][1] -= 1
            frame.after(1000, lambda: self.decrement_time(frame, address))
        else:
            self.mac_table.pop(address)

    def edit_device(self, port, device):
        self.ports[port - 1][0] = device.name
        self.ports[port - 1][1] = device.mac

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


