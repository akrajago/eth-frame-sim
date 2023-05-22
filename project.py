from tkinter import *
from Switch import Switch


def on_click_router(event):
    print("router")


def on_click_switch(event, name):
    print(name)


def add_device(type, horiz=False):
    pass


if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("750x500")

    device_info = Frame(root, width=200, height=200, relief=SUNKEN, bg="pink")
    device_info.pack()
    device_info_label = Label(device_info, text="hello")

    router = PhotoImage(file="img/router.png")
    router_label = Label(image=router)
    router_label.pack()
    router_label.bind("<Button-1>", on_click_router)

    switch_1 = Switch("Switch 1")
    switch_1_label = Label(image=switch_1.image)
    switch_1_label.pack()
    switch_1_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_1.name))

    switch_2 = Switch("Switch 2")
    switch_2_label = Label(image=switch_2.image)
    switch_2_label.pack()
    switch_2_label.bind("<Button-1>", lambda e: on_click_switch(e, switch_2.name))

    # router_btn = Button(root, text="New Ethernet frame", command=new_frame)
    # router_btn.place(x=20, y=20)
    # router_btn.pack()

    root.mainloop()


