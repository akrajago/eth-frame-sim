from tkinter import *
from Switch import Switch


def on_click_router(event):
    print("router")


def on_click_switch(event, switch, frame):
    # switch.highlight_device(event)
    switch.display_port_info(frame)

    add_port = Button(frame, text="Add device", command=add_device)
    add_port.grid(row=5, column=1)

    remove_port = Button(frame, text="Remove device", command=remove_device)
    remove_port.grid(row=5, column=2)


def add_device():
    editor = Tk()
    editor.title("Add device")
    editor.geometry("300x200")

    type_frame = Frame(editor)
    type_frame.grid(row=0, column=1)

    device_type = StringVar()

    switch = Radiobutton(type_frame, text="Switch", variable=device_type, value="switch")
    switch.pack()

    pc = Radiobutton(type_frame, text="PC", variable=device_type, value="pc")
    pc.pack()

    port_name = Entry(editor, width=20, fg='blue', font=('Arial', 16, 'bold'))
    port_name.grid(row=1, column=1)

    submit_btn = Button(editor, text="Add device", command=lambda: quit_window(editor, port_name, device_type))
    submit_btn.grid(row=5, column=1)


def remove_device():
    editor = Tk()
    editor.title("Remove device")
    editor.geometry("300x200")

    entry_label = Label(editor, width=15, text="Port #")
    entry_label.grid(row=0, column=0)

    port_number = Entry(editor, width=15, fg='blue', font=('Arial', 16, 'bold'))
    port_number.grid(row=0, column=1)

    # TODO: call switch function instead
    submit_btn = Button(editor, text="REMOVE device", command=lambda: quit_window(editor, "remove", port_number))
    submit_btn.grid(row=5, column=1)


def quit_window(frame, type, *args):
    print(type)
    for var in args:
        print(var.get())
    frame.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("750x500")

    device_info = Frame(root, width=200, height=200)
    device_info.pack()

    router = PhotoImage(file="img/router.png")
    router_label = Label(image=router)
    router_label.pack()
    router_label.bind("<Button-1>", on_click_router)

    switch_1 = Switch("Switch 1")
    switch_1.label.pack()
    switch_1.label.bind("<Button-1>", lambda e: on_click_switch(e, switch_1, device_info))

    switch_2 = Switch("Switch 2")
    switch_2.label.pack()
    switch_2.label.bind("<Button-1>", lambda e: on_click_switch(e, switch_2, device_info))

    root.mainloop()


