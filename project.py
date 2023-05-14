from tkinter import *

root = Tk()
root.title("Ethernet Frame Simulator")


def add_router():
    print("hi")


router_btn = Button(root, text="Add router", command=add_router)
router_btn.place(x=20, y=20)
router_btn.pack()

root.mainloop()


