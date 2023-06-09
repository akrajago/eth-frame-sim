from tkinter import *
from Switch import Switch
from Router import Router
from Pc import Pc
from Mac import Mac


def create_router(name, cnvs, lbls, mac):
    rtr = Router(name)
    rtr.place_router(cnvs, 1000, 200)
    cnvs.tag_bind(rtr.canvas_img, "<Button-1>", lambda e: on_click_router(e, rtr, lbls))
    cnvs.tag_bind(rtr.canvas_img, "<Double-Button-1>", lambda e: create_ethernet_frame(e, rtr, mac))
    # canvas.tag_bind(rtr.canvas_img, "<Enter>", rtr.highlight_device)
    # canvas.tag_bind(rtr.canvas_img, "<Leave>", rtr.unhighlight_device)
    return rtr


def create_switch(name, port, reference, cnvs, lbls, mac, hrzntl=False):
    swtch = Switch(name)
    if hrzntl:
        add_link(cnvs, reference, 1, swtch, 4, horizontal=True)
    else:
        add_link(cnvs, reference, port, swtch, port)

    cnvs.tag_bind(swtch.canvas_img, "<Button-1>", lambda e: on_click_switch(e, cnvs, lbls, mac, swtch, device_info))
    # swtch.pic_label.bind("<Enter>", swtch.highlight_device)
    # swtch.pic_label.bind("<Leave>", swtch.unhighlight_device)
    return swtch


def create_pc(name, port, reference, cnvs, mac):
    pc = Pc(name)
    add_link(cnvs, reference, port, pc, 0)
    cnvs.tag_bind(pc.canvas_img, "<Double-Button-1>", lambda e: create_ethernet_frame(e, pc, mac))
    return pc


def add_link(cnvs, device_1, port_1, device_2, port_2, horizontal=False):
    if horizontal:
        device_2.place_switch(cnvs, device_1.x - 500, device_1.y)
        device_2.ports[int(port_2) - 1][2] = device_1
        cnvs.create_line(device_2.port(port_2), device_2.y + 17,
                         device_1.port(port_1), device_1.y + 17, width=5)
    elif not port_2:
        device_2.place_pc(cnvs, device_1.port(port_1), device_1.y + 100)
        device_1.ports[int(port_1) - 1][2] = device_2
        cnvs.create_line(device_1.port(port_1), device_1.y + 100,
                         device_1.port(port_1), device_1.y + 17, width=5)
    else:
        device_2.place_switch(cnvs, device_1.x, device_1.y + 200)
        device_2.ports[int(port_1) - 1][2] = device_1
        device_1.ports[int(port_1) - 1][2] = device_2
        cnvs.create_line(device_2.port(port_2), device_2.y + 17,
                         device_1.port(port_1), device_1.y + 17, width=5)


def on_click_router(event, rtr, lbls):
    lbls[0][5].configure(text="")

    for i in range(2):
        lbls[0][i + 1].configure(text=i+1)
        lbls[1][i + 1].configure(text=rtr.ports[i])
        lbls[2][i + 1].configure(text="None")

        lbls[0][i + 3].configure(text="")
        lbls[1][i + 3].configure(text="")
        lbls[2][i + 3].configure(text="")

        if len(lbls[i + 1]) == 6:
            lbls[i + 1][5].grid_forget()


def on_click_switch(event, cnvs, lbls, mac, switch, frame):
    for i in range(4):
        lbls[0][i + 1].configure(text=i+1)
        lbls[1][i + 1].configure(text=switch.ports[i][0])
        lbls[2][i + 1].configure(text=switch.ports[i][1])

    lbls[0][5].configure(text=switch.name)

    lbls[1].append(Button(frame, text="Add device", command=lambda: add_device(frame, cnvs, lbls, mac, switch)))
    lbls[1][5].grid(row=5, column=1)

    lbls[2].append(Button(frame, text="Remove device", command=lambda: remove_device(frame, cnvs, lbls, mac, switch)))
    lbls[2][5].grid(row=5, column=2)


def set_port_info(frame):
    lbls = []

    col_0 = Frame(frame, width=20)
    col_0.grid(row=0, column=0)
    col0_label = Label(col_0, text="Port #", font=('Arial', 14, 'bold'))
    lbls.append([col0_label])

    col_1 = Frame(frame, width=20)
    col_1.grid(row=0, column=1)
    col1_label = Label(col_1, text="Device Name", font=('Arial', 14, 'bold'))
    lbls.append([col1_label])

    col_2 = Frame(frame, width=20)
    col_2.grid(row=0, column=2)
    col2_label = Label(col_2, text="Mac Address", font=('Arial', 14, 'bold'))
    lbls.append([col2_label])

    for i in range(4):
        port_num = Frame(frame, width=20)
        port_num.grid(row=i + 1, column=0)
        num_label = Label(port_num, text=f"")
        lbls[0].append(num_label)

        port_name = Frame(frame, width=20)
        port_name.grid(row=i + 1, column=1)
        name_label = Label(port_name, text="")
        lbls[1].append(name_label)

        port_mac = Frame(frame, width=20)
        port_mac.grid(row=i + 1, column=2)
        mac_label = Label(port_mac, text="")
        lbls[2].append(mac_label)

    switch_name = Frame(frame, width=20)
    switch_name.grid(row=5, column=0)
    switch_label = Label(switch_name, text="", font=('Arial', 14, 'bold'))
    lbls[0].append(switch_label)

    for column in lbls:
        for label in column:
            label.pack()

    return lbls


def create_ethernet_frame(event, device, mac):
    eframe = Tk()
    eframe.title("New Ethernet Frame")
    eframe.geometry("600x200")

    dest_mac_address = StringVar(eframe)
    source_mac_address = mac.get_mac(device.name)
    available = set(f"{address} [{name}]" for name, address in mac.known.items()) - {f"{source_mac_address} [{device.name}]"}

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
        submit_btn = Button(eframe, text="Send frame", command=lambda: quit_eth_window(eframe, dest_mac_address))

    dest_mac.grid(row=1, column=2, columnspan=2)

    submit_btn.grid(row=3, column=1, columnspan=2, pady=45)


def add_device(port_frame, cnvs, lbls, mac, switch):
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
                        command=lambda: quit_window(port_frame, editor, cnvs, lbls, mac, switch,
                                                    "add", port_number, device_type, port_name))
    submit_btn.grid(row=3, column=1, columnspan=2, pady=45)


def remove_device(port_frame, cnvs, lbls, mac, switch):
    editor = Tk()
    editor.title("Remove device")
    editor.geometry("300x200")

    entry_label = Label(editor, width=15, text="Port #")
    entry_label.grid(row=0, column=0, columnspan=2, pady=15)

    port_number = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
    port_number.grid(row=0, column=2, columnspan=2, pady=15)

    submit_btn = Button(editor, text="REMOVE device",
                        command=lambda: quit_window(port_frame, editor, cnvs, lbls, mac,
                                                    switch, "remove", port_number))
    submit_btn.grid(row=1, column=1, columnspan=2, padx=15, pady=45)


def quit_eth_window(frame, dest_mac):
    print(dest_mac.get().split())
    frame.destroy()


def quit_window(port_frame, frame, cnvs, lbls, mac, switch, edit_type, *args):
    inputs = []
    for var in args:
        inputs.append(var.get())

    frame.destroy()

    if edit_type == "add":
        lbls[1][int(inputs[0])].configure(text=inputs[2])

        if inputs[1] == "pc":
            mac_add = mac.create_mac(inputs[2])
            pc = create_pc(inputs[2], int(inputs[0]), switch, cnvs, mac)
            lbls[2][int(inputs[0])].configure(text=mac_add)
            switch.edit_device(int(inputs[0]), inputs[1], inputs[2], mac_add)
        else:
            switch.edit_device(int(inputs[0]), inputs[1], inputs[2], None)
            switch_new = create_switch(inputs[2], int(inputs[0]), switch, cnvs, lbls, mac)
            switch_new.edit_device(int(inputs[0]), inputs[1], switch.name, None)
    else:
        switch.remove_device(port_frame, int(inputs[0]))
        lbls[1][int(inputs[0])].configure(text="None")
        lbls[2][int(inputs[0])].configure(text="None")


if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("1500x1000")

    canvas = Canvas(root, width=1500, height=1000)
    canvas.place(x=0, y=0)

    device_info = Frame(root, width=200, height=150)
    device_info.pack()

    labels = set_port_info(device_info)
    mac_oracle = Mac()

    router = create_router("Router", canvas, labels, mac_oracle)
    switch_1 = create_switch("Switch 1", 4, router, canvas, labels, mac_oracle, hrzntl=True)
    router.edit_device(1, "switch", switch_1.name)
    switch_1.edit_device(4, "router", router.name, mac_oracle.create_mac(router.name))

    root.mainloop()

