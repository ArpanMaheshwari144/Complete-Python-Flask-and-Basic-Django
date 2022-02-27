from tkinter import *

def add():
    global i
    lb.insert(ACTIVE, f"{i}")   # ACTIVE->jo bhi listitem selected hai uske upar insert hoga
    i+=1

i = 0
root = Tk()
root.geometry("455x233")
root.title("Listbox tutorial")

lb = Listbox(root)
lb.pack()
lb.insert(END, "First item of our listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
