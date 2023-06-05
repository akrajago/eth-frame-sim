from tkinter import *


class Switch:

    def __init__(self, name):
        self.image = PhotoImage(file="img/switch.png")
        self.pic_label = Label(image=self.image)
        self.name = name
        self.ports = [["None", "None"] for i in range(4)]

    def highlight_device(self, event):
        self.pic_label.configure(bg="pink")

    def unhighlight_device(self, event):
        self.pic_label.configure(bg="white")

    def display_port_info(self, frame):
        if not len(self.col_labels):
            col_0 = Frame(frame, width=20)
            col_0.grid(row=0, column=0)
            col0_label = Label(col_0, text="Port #", font=('Arial', 14, 'bold'))
            self.col_labels.append([col0_label])

            col_1 = Frame(frame, width=20)
            col_1.grid(row=0, column=1)
            col1_label = Label(col_1, text="Device Name", font=('Arial', 14, 'bold'))
            self.col_labels.append([col1_label])

            col_2 = Frame(frame, width=20)
            col_2.grid(row=0, column=2)
            col2_label = Label(col_2, text="MAC Address", font=('Arial', 14, 'bold'))
            self.col_labels.append([col2_label])

            for i in range(4):
                port_num = Frame(frame, width=20)
                port_num.grid(row=i + 1, column=0)
                num_label = Label(port_num, text=f"{i + 1}")
                self.col_labels[0].append(num_label)

                port_name = Frame(frame, width=20)
                port_name.grid(row=i + 1, column=1)
                name_label = Label(port_name, text=f"{self.ports[i][0]}")
                self.col_labels[1].append(name_label)

                port_mac = Frame(frame, width=20)
                port_mac.grid(row=i + 1, column=2)
                mac_label = Label(port_mac, text=f"{self.ports[i][1]}")
                self.col_labels[2].append(mac_label)

        for column in self.col_labels:
            for label in column:
                label.pack()

        switch_name = Frame(frame, width=20)
        switch_name.grid(row=5, column=0)
        switch_label = Label(switch_name, text=f"{self.name}", bg="orange", font=('Arial', 14, 'bold'))
        switch_label.pack()

    def edit_device(self, frame, port, dev_type, name):
        self.ports[port - 1][0] = name
        print(dev_type)

    def remove_device(self, frame, port):
        self.ports[port - 1] = ["None", "None"]



