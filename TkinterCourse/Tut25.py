# Radio Buttons

from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

root.geometry("400x250")

root.title("Radio Buttons")

def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}, Thanks for ordering")

# var=IntVar() # isse hum value mei integer de sakte hai
var=StringVar()  # isse hum value mei string de sakte hai
var.set("Radio")  # ye isliye ki sare radiobuttons click na rahe hum kisi ek par hi click kar sake

Label(root, text="What would you like to have sir?", font="Lucida 16 bold", padx=14).pack(anchor="w")

radio=Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio=Radiobutton(root, text="Samosa", padx=14, variable=var, value="samosa").pack(anchor="w")
radio=Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio=Radiobutton(root, text="Ice Cream", padx=14, variable=var, value="Ice Cream").pack(anchor="w")
radio=Radiobutton(root, text="Cake", padx=14, variable=var, value="Cake").pack(anchor="w")
radio=Radiobutton(root, text="Bread Butter", padx=14, variable=var, value="Bread Butter").pack(anchor="w")

Button(root, text="Order Now", command=order).pack()

root.mainloop()