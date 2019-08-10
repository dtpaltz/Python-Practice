from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Tigers can live up to 300 years!')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like tigers?')
if answer == 'yes':
    print("Hurray!!!!!")
else:
    print("Booo!!!!")

root.mainloop()
