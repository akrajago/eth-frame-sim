from tkinter import *

root = Tk()
root.title("Ethernet Frame Simulator")
root.geometry("750x500")

device_info = Frame(root, width=200, height=200, relief=SUNKEN, bg="pink")
device_info.pack()
device_info_label = Label(device_info, text="hello")


def on_click(event=None):
    print("clicked")


def add_device(type, horiz=False):
    pass


router = PhotoImage(file="img/router.png")
router_label = Label(image=router)
router_label.pack()
router_label.bind("<Button-1>", on_click)

# router_btn = Button(root, text="New Ethernet frame", command=new_frame)
# router_btn.place(x=20, y=20)
# router_btn.pack()

root.mainloop()


