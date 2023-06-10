from tkinter import *
from Application import Application


def timer(frame, lbl):
    if t := lbl.cget("text"):
        lbl.configure(text=t-1)
        lbl.after(1000, lambda: timer(frame, lbl))


if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("1500x1000")

    app = Application(root)

    router = app.create_router("Router")
    switch_1 = app.create_switch("Switch 1", 4, router, hrzntl=True)
    router.edit_device(1, switch_1.name)
    switch_1.edit_device(4, "router", router.name, app.mac_oracle.create_mac(router.name))

    time_left = Label(app.mac_table, text=11)
    time_left.pack()

    timer(app.mac_table, time_left)

    root.mainloop()

