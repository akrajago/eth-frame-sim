from tkinter import *
from Switch import Switch
from Router import Router
from Pc import Pc
from Mac import Mac


class Application:

    def __init__(self, root):
        self.canvas = Canvas(root, width=1500, height=1000)
        self.canvas.place(x=0, y=0)

        self.device_info = Frame(root, width=200, height=150)
        self.device_info.pack()

        self.mac_table = Frame(root, width=300, height=250, bg="pink")
        self.mac_table.place(x=0, y=0)

        self.labels = []
        self.devices = []
        self.mac_oracle = Mac()

        self.set_port_info(self.device_info)

    def create_router(self, name):
        rtr = Router(name)
        self.devices.append(rtr)
        rtr.place_router(self.canvas, 1000, 200)
        self.canvas.tag_bind(rtr.canvas_img, "<Button-1>", lambda e: self.on_click_router(e, rtr))
        self.canvas.tag_bind(rtr.canvas_img, "<Double-Button-1>", lambda e: self.create_ethernet_frame(e, rtr))
        # canvas.tag_bind(rtr.canvas_img, "<Enter>", rtr.highlight_device)
        # canvas.tag_bind(rtr.canvas_img, "<Leave>", rtr.unhighlight_device)
        return rtr

    def create_switch(self, name, port, reference, hrzntl=False):
        swtch = Switch(name)
        self.devices.append(swtch)

        if hrzntl:
            self.add_link(reference, 1, swtch, 4, horizontal=True)
        else:
            self.add_link(reference, port, swtch, port)

        self.canvas.tag_bind(swtch.canvas_img, "<Button-1>", lambda e: self.on_click_switch(e, swtch))
        # swtch.pic_label.bind("<Enter>", swtch.highlight_device)
        # swtch.pic_label.bind("<Leave>", swtch.unhighlight_device)
        return swtch

    def create_pc(self, name, port, reference):
        pc = Pc(name)
        self.add_link(reference, port, pc, 0)
        self.canvas.tag_bind(pc.canvas_img, "<Double-Button-1>", lambda e: self.create_ethernet_frame(e, pc))
        return pc

    def add_link(self, device_1, port_1, device_2, port_2, horizontal=False):
        if horizontal:
            device_2.place_switch(self.canvas, device_1.x - 500, device_1.y)
            device_2.ports[int(port_2) - 1][2] = device_1
            self.canvas.create_line(device_2.port(port_2), device_2.y + 17,
                                    device_1.port(port_1), device_1.y + 17, width=5)
        elif not port_2:
            device_2.place_pc(self.canvas, device_1.port(port_1), device_1.y + 100)
            device_1.ports[int(port_1) - 1][2] = device_2
            self.canvas.create_line(device_1.port(port_1), device_1.y + 100,
                                    device_1.port(port_1), device_1.y + 17, width=5)
        else:
            device_2.place_switch(self.canvas, device_1.x, device_1.y + 200)
            device_2.ports[int(port_1) - 1][2] = device_1
            device_1.ports[int(port_1) - 1][2] = device_2
            self.canvas.create_line(device_2.port(port_2), device_2.y + 17,
                                    device_1.port(port_1), device_1.y + 17, width=5)

    def on_click_router(self, event, rtr):
        self.labels[0][5].configure(text="")

        for i in range(2):
            self.labels[0][i + 1].configure(text=i + 1)
            self.labels[1][i + 1].configure(text=rtr.ports[i])
            self.labels[2][i + 1].configure(text="None")

            self.labels[0][i + 3].configure(text="")
            self.labels[1][i + 3].configure(text="")
            self.labels[2][i + 3].configure(text="")

            if self.labels[i + 1][5]:
                self.labels[i + 1][5].grid_forget()

    def on_click_switch(self, event, switch):
        for i in range(4):
            self.labels[0][i + 1].configure(text=i + 1)
            self.labels[1][i + 1].configure(text=switch.ports[i][0])
            self.labels[2][i + 1].configure(text=switch.ports[i][1])

        self.labels[0][5].configure(text=switch.name)

        self.labels[1][5] = Button(self.device_info, text="Add device", command=lambda: self.add_device(switch))
        self.labels[1][5].grid(row=5, column=1)

        self.labels[2][5] = Button(self.device_info, text="Remove device", command=lambda: self.remove_device(switch))
        self.labels[2][5].grid(row=5, column=2)

    def set_port_info(self, frame):
        col_0 = Frame(frame, width=20)
        col_0.grid(row=0, column=0)
        col0_label = Label(col_0, text="Port #", font=("Arial", 14, "bold"))
        self.labels.append([col0_label])

        col_1 = Frame(frame, width=20)
        col_1.grid(row=0, column=1)
        col1_label = Label(col_1, text="Device Name", font=("Arial", 14, "bold"))
        self.labels.append([col1_label])

        col_2 = Frame(frame, width=20)
        col_2.grid(row=0, column=2)
        col2_label = Label(col_2, text="Mac Address", font=("Arial", 14, "bold"))
        self.labels.append([col2_label])

        for i in range(4):
            port_num = Frame(frame, width=20)
            port_num.grid(row=i + 1, column=0)
            num_label = Label(port_num, text=f"")
            self.labels[0].append(num_label)

            port_name = Frame(frame, width=20)
            port_name.grid(row=i + 1, column=1)
            name_label = Label(port_name, text="")
            self.labels[1].append(name_label)

            port_mac = Frame(frame, width=20)
            port_mac.grid(row=i + 1, column=2)
            mac_label = Label(port_mac, text="")
            self.labels[2].append(mac_label)

        switch_name = Frame(frame, width=20)
        switch_name.grid(row=5, column=0)
        switch_label = Label(switch_name, text="", font=("Arial", 14, "bold"))
        self.labels[0].append(switch_label)

        for column in self.labels:
            for label in column:
                label.pack()

        self.labels[1].append(None)
        self.labels[2].append(None)

    def create_ethernet_frame(self, event, device):
        eframe = Tk()
        eframe.title("New Ethernet Frame")
        eframe.geometry("600x200")

        dest_mac_address = StringVar(eframe)
        source_mac_address = self.mac_oracle.get_mac(device.name)
        available = set(f"{address} [{name}]" for name, address
                        in self.mac_oracle.known.items()) - \
                    {f"{source_mac_address} [{device.name}]"}

        source_label = Label(eframe, width=30, text="Source MAC Address")
        source_label.grid(row=0, column=0, columnspan=2, pady=10)

        dest_label = Label(eframe, width=30, text="Destination MAC Address")
        dest_label.grid(row=0, column=2, columnspan=2, pady=10)

        source_mac = Label(eframe, width=30, text=source_mac_address)
        source_mac.grid(row=1, column=0, columnspan=2)

        if not available:
            dest_mac = Label(eframe, width=30, text="Not enough devices in network")
            submit_btn = Button(eframe, text="Close", command=lambda: eframe.destroy())
        else:
            dest_mac = OptionMenu(eframe, dest_mac_address, *available)
            submit_btn = Button(eframe, text="Send frame",
                                command=lambda: self.quit_eth_window(eframe, source_mac_address, dest_mac_address))

        dest_mac.grid(row=1, column=2, columnspan=2)

        submit_btn.grid(row=3, column=1, columnspan=2, pady=45)

    def forward_frame(self, source_mac, dest_mac):
        # Is source address in MAC table? If no, add it; else reset timer
        # Is destination address in MAC table? If yes, forward it out corresponding port; else forward out all ports
        print(source_mac, dest_mac)

    def add_device(self, switch):
        editor = Tk()
        editor.title("Add device")
        editor.geometry("300x200")

        device_type = StringVar(editor)

        switch_opt = Radiobutton(editor, text="Switch", variable=device_type, value="switch")
        switch_opt.grid(row=0, column=0, columnspan=2, pady=15)

        pc_opt = Radiobutton(editor, text="PC", variable=device_type, value="pc")
        pc_opt.grid(row=0, column=2, columnspan=2, pady=15)

        number_label = Label(editor, width=10, text="Port #")
        number_label.grid(row=1, column=0, columnspan=2)

        port_number = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
        port_number.grid(row=1, column=2, columnspan=2)

        name_label = Label(editor, width=15, text="Device Name")
        name_label.grid(row=2, column=0, columnspan=2)

        port_name = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
        port_name.grid(row=2, column=2, columnspan=2)

        submit_btn = Button(editor, text="Add device",
                            command=lambda: self.quit_window(editor, switch, "add", port_number,
                                                             device_type, port_name))
        submit_btn.grid(row=3, column=1, columnspan=2, pady=45)

    def remove_device(self, switch):
        editor = Tk()
        editor.title("Remove device")
        editor.geometry("300x200")

        entry_label = Label(editor, width=15, text="Port #")
        entry_label.grid(row=0, column=0, columnspan=2, pady=15)

        port_number = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
        port_number.grid(row=0, column=2, columnspan=2, pady=15)

        submit_btn = Button(editor, text="REMOVE device",
                            command=lambda: self.quit_window(editor, switch, "remove", port_number))
        submit_btn.grid(row=1, column=1, columnspan=2, padx=15, pady=45)

    def quit_eth_window(self, frame, device, source_mac, dest_mac_info):
        dest_mac = dest_mac_info.get().split()[0]
        frame.destroy()
        self.forward_frame(device, source_mac, dest_mac)

    def quit_window(self, frame, switch, edit_type, *args):
        inputs = []
        for var in args:
            inputs.append(var.get())

        frame.destroy()

        if edit_type == "add":
            self.labels[1][int(inputs[0])].configure(text=inputs[2])

            if inputs[1] == "pc":
                mac_add = self.mac_oracle.create_mac(inputs[2])
                pc = self.create_pc(inputs[2], int(inputs[0]), switch)
                pc.edit_device(switch)
                self.labels[2][int(inputs[0])].configure(text=mac_add)
                switch.edit_device(int(inputs[0]), inputs[1], inputs[2], mac_add)
            else:
                switch.edit_device(int(inputs[0]), inputs[1], inputs[2], "None")
                switch_new = self.create_switch(inputs[2], int(inputs[0]), switch)
                self.devices.append(switch_new)
                switch_new.edit_device(int(inputs[0]), inputs[1], switch.name, "None")
        else:
            switch.remove_device(int(inputs[0]))
            self.labels[1][int(inputs[0])].configure(text="None")
            self.labels[2][int(inputs[0])].configure(text="None")
