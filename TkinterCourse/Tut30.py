from tkinter import *

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set("Ready After Busy")

root=Tk()     # hum yaha Tk() class ke constructor ko call karte hai
root.geometry("455x233")
root.title("Status Bar")

statusvar=StringVar()
statusvar.set("Ready Before Busy")

sbar=Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()