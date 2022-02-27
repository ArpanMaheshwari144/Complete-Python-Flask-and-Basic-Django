from tkinter import *

# Class GUI inherited Tk class
class GUI(Tk):
    def __init__(self):    # Jo phle yaha root the wo ab is class ke andar self ho gya hai
        super().__init__()
        self.geometry("744x377")

    def status(self):
        var = StringVar()
        var.set("Radio")
        Label(self, text="What would you like to have sir?", font="Lucida 16 bold", padx=14).pack(anchor="w")
        list = ["Chowmin", "Pasta", "Menchuriun", "Chilli", "Dosa"]

        for item in list:
            radio = Radiobutton(self, text=f"{item}", variable=var, value=f"{item}", font="lucida 9").pack(anchor="w")

    def order(self):
        print("Order Recieved!")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.order).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Order Now")
    window.mainloop()