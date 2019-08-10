from tkinter import *

class GuiButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Msg", command=self.print_message)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


    def print_message(self):
        print("Wow! This actually worked!")


root = Tk()
b = GuiButtons(root)
root.mainloop()


