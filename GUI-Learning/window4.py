from tkinter import *

root = Tk()


def print_name(event):
    print("My name is Dustin!")


button_1 = Button(root, text="Print Name")
button_1.bind("<Button-1>", print_name)  # <Button-1> == left mouse button
button_1.pack()


root.mainloop()