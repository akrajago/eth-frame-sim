from tkinter import *
from Switch import Switch


def on_click_router(event):
    print("router")


def on_click_switch(event, switch, frame):
    # TODO: display ports and MAC address table
    print(f"{switch.name}")

    col_0 = Frame(frame, width=20)
    col_0.grid(row=0, column=0)
    col0_label = Label(col_0, text="Port #")
    col0_label.pack()

    col_1 = Frame(frame, width=20)
    col_1.grid(row=0, column=1)
    col1_label = Label(col_1, text="Device Name")
    col1_label.pack()

    for i in range(4):
        port_num = Frame(frame, width=20)
        port_num.grid(row=i + 1, column=0)
        num_label = Label(port_num, text=f"{i + 1}")
        num_label.pack()

        port_name = Frame(frame, width=20)
        port_name.grid(row=i + 1, column=1)
        name_label = Label(port_name, text=f"{switch.ports[i]}")
        name_label.pack()

    edit_port = Button(frame, text="Edit device", command=edit_device)
    edit_port.grid(row=5, column=0)

    remove_port = Button(frame, text="Remove device", command=remove_device)
    remove_port.grid(row=5, column=1)


def edit_device():
    editor = Tk()
    editor.title("Edit device")
    editor.geometry("300x200")

    port_name = Entry(editor, width=20, fg='blue', font=('Arial', 16, 'bold'))
    port_name.grid(row=0, column=1)


def remove_device():
    print("remove device")


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
    switch_1_label = Label(image=switch_1.image)
    switch_1_label.pack()
    switch_1_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_1, device_info))

    switch_2 = Switch("Switch 2")
    switch_2_label = Label(image=switch_2.image)
    switch_2_label.pack()
    switch_2_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_2, device_info))

    # router_btn = Button(root, text="New Ethernet frame", command=new_frame)
    # router_btn.place(x=20, y=20)
    # router_btn.pack()

    root.mainloop()


