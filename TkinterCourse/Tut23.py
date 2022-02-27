from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

root.geometry("455x233")

root.title("Sliders")

def getdollar():
    print(f"We have credited {myslider2.get()} doolars to your bank account")
    tmsg.showinfo("Amount Credited", f"We have credited {myslider2.get()} doolars to your bank account")


# Vertical Slider
# myslider1=Scale(root, from_=0, to=100)
# myslider1.pack()

# Horizontal Slider
Label(root, text="How many dollars do you want?").pack()

# myslider2=Scale(root, from_=0, to=100, orient=HORIZONTAL)
myslider2=Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)

# myslider2.set(10)

myslider2.pack()

Button(root, text="Get Dollars!", pady=10, command=getdollar).pack()

root.mainloop()
