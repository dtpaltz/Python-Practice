from tkinter import *

root = Tk()

def left_click(event):
    print("LEFT")

def middle_click(event):
    print("MIDDLE")

def right_click(event):
    print("RIGHT")


frame = Frame(root, width=300, height=250, bg='green')
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()


root.mainloop()
