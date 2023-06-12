from tkinter import *
from Application import Application

if __name__ == "__main__":
    root = Tk()
    root.title("Ethernet Frame Simulator")
    root.geometry("1500x1000")

    app = Application(root)

    router = app.create_router("Router")
    switch_1 = app.create_switch("Switch 1", 4, router, hrzntl=True)
    router.edit_device(1, switch_1, app.mac_oracle.create_mac(router.name))
    switch_1.edit_device(4, router)

    root.mainloop()

