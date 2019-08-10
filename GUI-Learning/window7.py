from tkinter import *

def do_nothing():
    print("Do nothing")

root = Tk()

menu_bar = Menu(root, tearoff=False)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project...", command=do_nothing)
file_menu.add_command(label="New", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=do_nothing)

edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=do_nothing)

root.mainloop()
