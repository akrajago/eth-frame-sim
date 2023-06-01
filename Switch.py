from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.label = Label(image=self.image)
        self.name = name
        self.ports = [None] * 4
        self.mac_addresses = [None] * 4

    # def highlight_device(self, event):
    #     self.label.configure(bg="pink")

    def display_port_info(self, frame):
        col_0 = Frame(frame, width=20)
        col_0.grid(row=0, column=0)
        col0_label = Label(col_0, text="Port #", font=('Arial', 14, 'bold'))
        col0_label.pack()

        col_1 = Frame(frame, width=20)
        col_1.grid(row=0, column=1)
        col1_label = Label(col_1, text="Device Name", font=('Arial', 14, 'bold'))
        col1_label.pack()

        col_2 = Frame(frame, width=20)
        col_2.grid(row=0, column=2)
        col2_label = Label(col_2, text="Mac Address", font=('Arial', 14, 'bold'))
        col2_label.pack()

        for i in range(4):
            port_num = Frame(frame, width=20)
            port_num.grid(row=i+1, column=0)
            num_label = Label(port_num, text=f"{i + 1}")
            num_label.pack()

            port_name = Frame(frame, width=20)
            port_name.grid(row=i+1, column=1)
            name_label = Label(port_name, text=f"{self.ports[i]}")
            name_label.pack()

            port_mac = Frame(frame, width=20)
            port_mac.grid(row=i+1, column=2)
            mac_label = Label(port_mac, text=f"{self.mac_addresses[i]}")
            mac_label.pack()

        switch_name = Frame(frame, width=20)
        switch_name.grid(row=5, column=0)
        switch_label = Label(switch_name, text=f"{self.name}", bg="orange", font=('Arial', 14, 'bold'))
        switch_label.pack()

    def edit_device(self, port, name):
        self.ports[port - 1] = name
