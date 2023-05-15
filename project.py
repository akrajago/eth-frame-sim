from tkinter import *

root = Tk()
root.title("Ethernet Frame Simulator")
root.geometry("750x500")

device_info = Frame(root, width=200, height=200, relief=SUNKEN, bg="blue")
device_info.pack()


def add_router():
    print("hi")


def on_click(event=None):
    print("clicked")


router = PhotoImage(file="img/router.png")
router_label = Label(image=router)
router_label.pack()
router_label.bind("<Button-1>", on_click)

router_btn = Button(root, text="Add router", command=add_router)
router_btn.place(x=20, y=20)
router_btn.pack()

root.mainloop()


