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

# ********** Toolbar ************

toolbar = Frame(root, bg="blue")

insertBt = Button(toolbar, text="Insert Image", command=do_nothing)
insertBt.pack(side=LEFT, padx=2, pady=2)
printBt = Button(toolbar, text="Print", command=do_nothing)
printBt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


# ****************** Status Bar ******************

status = Label(root, text="Pending...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)




root.mainloop()
