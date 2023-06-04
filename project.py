from tkinter import *
from Switch import Switch


def on_click_router(event):
    print("router")


def on_click_switch(event, switch, frame):
    switch.display_port_info(frame)

    add_switch = Button(frame, text="Add device", command=lambda: add_device(frame, switch))
    add_switch.grid(row=5, column=1)

    remove_port = Button(frame, text="Remove device", command=lambda: remove_device(frame, switch))
    remove_port.grid(row=5, column=2)


def add_device(port_frame, switch):
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
                        command=lambda: quit_window(port_frame, editor, switch,
                                                    "add", port_number, device_type, port_name))
    submit_btn.grid(row=3, column=1, columnspan=2, pady=45)


def remove_device(port_frame, switch):
    editor = Tk()
    editor.title("Remove device")
    editor.geometry("300x200")

    entry_label = Label(editor, width=15, text="Port #")
    entry_label.grid(row=0, column=0, columnspan=2, pady=15)

    port_number = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
    port_number.grid(row=0, column=2, columnspan=2, pady=15)

    submit_btn = Button(editor, text="REMOVE device",
                        command=lambda: quit_window(port_frame, editor, switch, "remove", port_number))
    submit_btn.grid(row=1, column=1, columnspan=2, padx=15, pady=45)


def quit_window(port_frame, frame, switch, edit_type, *args):
    inputs = []
    for var in args:
        inputs.append(var.get())

    if edit_type == "add":
        switch.edit_device(port_frame, int(inputs[0]), inputs[1], inputs[2])
    else:
        switch.remove_device(port_frame, int(inputs[0]))

    frame.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("750x500")

    device_info = Frame(root, width=200, height=150)
    device_info.pack()

    router = PhotoImage(file="img/router.png")
    router_label = Label(image=router)
    router_label.pack()
    router_label.bind("<Button-1>", on_click_router)

    switch_1 = Switch("Switch 1")
    switch_1.pic_label.pack()
    switch_1.pic_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_1, device_info))
    switch_1.pic_label.bind("<Enter>", switch_1.highlight_device)
    switch_1.pic_label.bind("<Leave>", switch_1.unhighlight_device)

    switch_2 = Switch("Switch 2")
    switch_2.pic_label.pack()
    switch_2.pic_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_2, device_info))

    root.mainloop()


