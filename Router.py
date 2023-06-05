from tkinter import *


class Router:

    def __init__(self, name):
        self.image = PhotoImage(file="img/router.png")
        self.pic_label = Label(image=self.image)
        self.name = name
        self.ports = ["None", "None"]
        self.x = None
        self.y = None

    def highlight_device(self, event):
        self.pic_label.configure(bg="pink")

    def unhighlight_device(self, event):
        self.pic_label.configure(bg="white")

    def display_port_info(self, frame):
        col_0 = Frame(frame, width=20)
        col_0.grid(row=0, column=0)
        col0_label = Label(col_0, text="Port #", font=('Arial', 14, 'bold'))
        col0_label.pack()

        col_1 = Frame(frame, width=20)
        col_1.grid(row=0, column=1)
        col1_label = Label(col_1, text="Device Name", font=('Arial', 14, 'bold'))
        col1_label.pack()

        for i in range(2):
            port_num = Frame(frame, width=20)
            port_num.grid(row=i + 1, column=0)
            num_label = Label(port_num, text=f"{i + 1}")
            num_label.pack()

            port_name = Frame(frame, width=20)
            port_name.grid(row=i + 1, column=1)
            name_label = Label(port_name, text=f"{self.ports[i]}")
            name_label.pack()

        switch_name = Frame(frame, width=20)
        switch_name.grid(row=5, column=0)
        switch_label = Label(switch_name, text=f"{self.name}", bg="orange", font=('Arial', 14, 'bold'))
        switch_label.pack()

    def place_router(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.pic_label.place(x=x_coord, y=y_coord)
