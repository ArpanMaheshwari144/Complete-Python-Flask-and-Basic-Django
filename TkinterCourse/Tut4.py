from tkinter import *
from PIL import Image, ImageTk   # PIL means pillow-> jo ki jpg images ko tkinter mei kholne ke liye help karta hai

arpan_root=Tk()

arpan_root.geometry("1255x944")

# for png images:
# photo =PhotoImage(file="social.png")

# for jpg images:
image=Image.open("city.jpg")
photo=ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()

arpan_root.mainloop()
