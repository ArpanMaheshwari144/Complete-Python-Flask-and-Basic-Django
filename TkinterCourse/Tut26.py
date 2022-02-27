# Radio Button with For loop
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("400x250")
root.title("Radio Button in Tkinter")

def order():
    msg.showinfo("Order Recieved!", f"We have received your order for {var.get()}. Thanks for your ordering.")

var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have sir?",  font="Lucida 16 bold", padx=14).pack(anchor="w")
list = ["Chowmin", "Pasta", "Menchuriun", "Chilli", "Dosa"]

for item in list:
    radio = Radiobutton(root, text=f"{item}", variable=var, value=f"{item}", font="lucida 9").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root.mainloop()