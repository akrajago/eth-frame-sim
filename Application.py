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

        self.mac_info = Frame(root, width=300, height=250)
        self.mac_info.place(x=0, y=0)

        self.port_labels = []
        self.mac_labels = []
        self.devices = []
        self.mac_oracle = Mac()

        self.set_port_info()
        self.set_mac_info()

    def create_router(self, name):
        rtr = Router(name)
        self.devices.append(rtr)
        rtr.place_router(self.canvas, 1000, 200)
        self.canvas.tag_bind(rtr.canvas_img, "<Button-1>",
                             lambda e: self.on_click_router(rtr))
        self.canvas.tag_bind(rtr.canvas_img, "<Double-Button-1>",
                             lambda e: self.create_ethernet_frame(rtr))
        self.canvas.tag_bind(rtr.canvas_img, "<Enter>",
                             lambda e: rtr.highlight_router(self.canvas))
        self.canvas.tag_bind(rtr.canvas_img, "<Leave>",
                             lambda e: rtr.unhighlight_router(self.canvas))
        return rtr

    def create_switch(self, name, port, reference, hrzntl=False):
        swtch = Switch(name)
        self.devices.append(swtch)

        if hrzntl:
            self.add_link(reference, 1, swtch, 4, horizontal=True)
        else:
            self.add_link(reference, port, swtch, port)

        self.canvas.tag_bind(swtch.canvas_img, "<Button-1>",
                             lambda e: self.on_click_switch(swtch))
        self.canvas.tag_bind(swtch.canvas_img, "<Enter>",
                             lambda e: swtch.highlight_switch(self.canvas))
        self.canvas.tag_bind(swtch.canvas_img, "<Leave>",
                             lambda e: swtch.unhighlight_switch(self.canvas))
        return swtch

    def create_pc(self, name, port, reference):
        pc = Pc(name)
        self.add_link(reference, port, pc, 0)
        self.canvas.tag_bind(pc.canvas_img, "<Double-Button-1>",
                             lambda e: self.create_ethernet_frame(pc))
        self.canvas.tag_bind(pc.canvas_img, "<Enter>",
                             lambda e: pc.highlight_pc(self.canvas))
        self.canvas.tag_bind(pc.canvas_img, "<Leave>",
                             lambda e: pc.unhighlight_pc(self.canvas))
        return pc

    def highlight(self, device, found=False):
        if not found:
            self.canvas.itemconfigure(device.canvas_img, image=device.image_red)
        else:
            self.canvas.itemconfigure(device.canvas_img, image=device.image_green)
        self.canvas.after(1000, lambda: self.canvas.itemconfigure(device.canvas_img,
                                                                  image=device.image))

    def add_link(self, device_1, port_1, device_2, port_2, horizontal=False):
        if horizontal:
            device_2.place_switch(self.canvas, device_1.x - 500, device_1.y)
            device_2.ports[int(port_2) - 1][2] = device_1
            self.canvas.create_line(device_2.port(port_2), device_2.y + 17,
                                    device_1.port(port_1), device_1.y + 17, width=5)
        elif not port_2:
            device_2.place_pc(self.canvas, device_1,
                              device_1.port(port_1), device_1.y + 100)
            device_1.ports[int(port_1) - 1][2] = device_2
            self.canvas.create_line(device_1.port(port_1), device_1.y + 100,
                                    device_1.port(port_1), device_1.y + 17, width=5)
        else:
            device_2.place_switch(self.canvas, device_1.x, device_1.y + 200)
            device_2.ports[int(port_1) - 1][2] = device_1
            device_1.ports[int(port_1) - 1][2] = device_2
            self.canvas.create_line(device_2.port(port_2), device_2.y + 17,
                                    device_1.port(port_1), device_1.y + 17, width=5)

    def on_click_router(self, rtr):
        self.port_labels[0][5].configure(text="")

        for i in range(2):
            self.port_labels[0][i + 1].configure(text=i + 1)
            self.port_labels[1][i + 1].configure(text=rtr.ports[i][0])
            self.port_labels[2][i + 1].configure(text="None")

            self.port_labels[0][i + 3].configure(text="")
            self.port_labels[1][i + 3].configure(text="")
            self.port_labels[2][i + 3].configure(text="")

            if self.port_labels[i + 1][5]:
                self.port_labels[i + 1][5].grid_forget()

        for j in range(10):
            self.mac_labels[0][j + 1].configure(text="")
            self.mac_labels[1][j + 1].configure(text="")

    def on_click_switch(self, switch):
        for i in range(4):
            self.port_labels[0][i + 1].configure(text=i + 1)
            self.port_labels[1][i + 1].configure(text=switch.ports[i][0])
            self.port_labels[2][i + 1].configure(text=switch.ports[i][1])

        self.port_labels[0][5].configure(text=switch.name)

        self.port_labels[1][5] = Button(self.device_info, text="Add device",
                                        command=lambda: self.add_device(switch))
        self.port_labels[1][5].grid(row=5, column=1)

        # self.port_labels[2][5] = Button(self.device_info, text="Remove device",
        #                                 command=lambda: self.remove_device(switch))
        # self.port_labels[2][5].grid(row=5, column=2)

        for i, address in enumerate(switch.mac_table):
            self.mac_labels[0][i + 1].configure(text=address)
            self.mac_labels[1][i + 1].configure(text=switch.mac_table[address][0])
            self.mac_labels[2][i + 1].configure(text=switch.mac_table[address][1])

        for j in range(len(switch.mac_table), 10):
            self.mac_labels[0][j + 1].configure(text="")
            self.mac_labels[1][j + 1].configure(text="")
            self.mac_labels[2][j + 1].configure(text="")

    def set_port_info(self):
        col_0 = Frame(self.device_info, width=20)
        col_0.grid(row=0, column=0)
        col0_label = Label(col_0, text="Port #", font=("Arial", 14, "bold"))
        self.port_labels.append([col0_label])

        col_1 = Frame(self.device_info, width=20)
        col_1.grid(row=0, column=1)
        col1_label = Label(col_1, text="Device Name", font=("Arial", 14, "bold"))
        self.port_labels.append([col1_label])

        col_2 = Frame(self.device_info, width=20)
        col_2.grid(row=0, column=2)
        col2_label = Label(col_2, text="Mac Address", font=("Arial", 14, "bold"))
        self.port_labels.append([col2_label])

        for i in range(4):
            port_num = Frame(self.device_info, width=20)
            port_num.grid(row=i + 1, column=0)
            num_label = Label(port_num, text=f"")
            self.port_labels[0].append(num_label)

            port_name = Frame(self.device_info, width=20)
            port_name.grid(row=i + 1, column=1)
            name_label = Label(port_name, text="")
            self.port_labels[1].append(name_label)

            port_mac = Frame(self.device_info, width=20)
            port_mac.grid(row=i + 1, column=2)
            mac_label = Label(port_mac, text="")
            self.port_labels[2].append(mac_label)

        switch_name = Frame(self.device_info, width=20)
        switch_name.grid(row=5, column=0)
        switch_label = Label(switch_name, text="", font=("Arial", 14, "bold"))
        self.port_labels[0].append(switch_label)

        for column in self.port_labels:
            for label in column:
                label.pack()

        self.port_labels[1].append(None)
        self.port_labels[2].append(None)

    def set_mac_info(self):
        col_0 = Frame(self.mac_info, width=20)
        col_0.grid(row=0, column=0)
        col0_label = Label(col_0, text="Mac Address", font=("Arial", 14, "bold"))
        self.mac_labels.append([col0_label])

        col_1 = Frame(self.mac_info, width=20)
        col_1.grid(row=0, column=1)
        col1_label = Label(col_1, text="Port #", font=("Arial", 14, "bold"))
        self.mac_labels.append([col1_label])

        col_2 = Frame(self.mac_info, width=20)
        col_2.grid(row=0, column=2)
        col2_label = Label(col_2, text="Time Left", font=("Arial", 14, "bold"))
        self.mac_labels.append([col2_label])

        for i in range(10):
            mac_add = Frame(self.mac_info, width=20)
            mac_add.grid(row=i + 1, column=0)
            address_label = Label(mac_add, text=f"")
            self.mac_labels[0].append(address_label)

            port_num = Frame(self.mac_info, width=20)
            port_num.grid(row=i + 1, column=1)
            port_label = Label(port_num, text="")
            self.mac_labels[1].append(port_label)

            time_left = Frame(self.mac_info, width=20)
            time_left.grid(row=i + 1, column=2)
            time_label = Label(time_left, text="")
            self.mac_labels[2].append(time_label)

        for column in self.mac_labels:
            for label in column:
                label.pack()

    def create_ethernet_frame(self, device):
        eframe = Tk()
        eframe.title("New Ethernet Frame")
        eframe.geometry("600x200")

        dest_mac_address = StringVar(eframe)
        source_mac_address = self.mac_oracle.get_mac(device.name)
        available = set(f"{address} [{name}]" for name, address
                        in self.mac_oracle.known.items()) \
                    - {f"{source_mac_address} [{device.name}]"}

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
                                command=lambda: self.quit_eth_window(eframe, device,
                                                                     source_mac_address,
                                                                     dest_mac_address))

        dest_mac.grid(row=1, column=2, columnspan=2)

        submit_btn.grid(row=3, column=1, columnspan=2, pady=45)

    def forward_frame(self, device, source_mac, dest_mac, port=0):
        self.highlight(device)
        if isinstance(device, Router):
            if device.mac == source_mac:
                self.forward_frame(device.ports[0][1], source_mac, dest_mac, port=4)
            elif device.mac == dest_mac:
                self.highlight(device, found=True)
        elif isinstance(device, Pc):
            if device.mac == source_mac:
                self.forward_frame(device.switch, source_mac, dest_mac, port=device.port)
            elif device.mac == dest_mac:
                self.highlight(device, found=True)
        else:
            if source_mac in device.mac_table:
                device.reset_timer(self.mac_info, source_mac)
            else:
                device.add_mac_entry(self.mac_info, source_mac, port)

            if dest_mac in device.mac_table:
                self.forward_frame(device.ports[device.mac_table[dest_mac][0] - 1][2],
                                   source_mac, dest_mac,
                                   port=device.mac_table[dest_mac][0])
            else:
                for i in range(4):
                    if (i + 1) != port and device.ports[i][0] != "None":
                        self.forward_frame(device.ports[i][2], source_mac,
                                           dest_mac, port=i + 1)

    def add_device(self, switch):
        editor = Tk()
        editor.title("Add device")
        editor.geometry("300x200")

        device_type = StringVar(editor)

        switch_opt = Radiobutton(editor, text="Switch", variable=device_type,
                                 value="switch")
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
                            command=lambda: self.quit_window(editor, switch, "add",
                                                             port_number, device_type, port_name))
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
                            command=lambda: self.quit_window(editor, switch,
                                                             "remove", port_number))
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
            self.port_labels[1][int(inputs[0])].configure(text=inputs[2])

            if inputs[1] == "pc":
                mac_add = self.mac_oracle.create_mac(inputs[2])
                pc = self.create_pc(inputs[2], int(inputs[0]), switch)
                pc.set_info(int(inputs[0]), mac_add)
                self.port_labels[2][int(inputs[0])].configure(text=mac_add)
                switch.edit_device(int(inputs[0]), pc)
            else:
                switch_new = self.create_switch(inputs[2], int(inputs[0]), switch)
                self.devices.append(switch_new)
                switch.edit_device(int(inputs[0]), switch_new)
                switch_new.edit_device(int(inputs[0]), switch)
        else:
            switch.remove_device(int(inputs[0]))
            self.port_labels[1][int(inputs[0])].configure(text="None")
            self.port_labels[2][int(inputs[0])].configure(text="None")
