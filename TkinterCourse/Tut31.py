# Using Classes And Objects To Create GUIs
# Classes and Objects create GUi's encapsuled(implement details GUI ke andar band hai)

from tkinter import *

# Class GUI inherited Tk class
class GUI(Tk):
    def __init__(self):    # Jo phle yaha root the wo ab is class ke andar self ho gya hai
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button is Clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()    # Jo phle yaha root the ab wo window ho gaya hai


