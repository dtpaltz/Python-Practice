from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

black_line = canvas.create_line(0, 0, 200, 50)
red_line = canvas.create_line(0, 100, 200, 50, fill="red")
green_box = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# canvas.delete(red_line)
# canvas.delete(ALL)

root.mainloop()
