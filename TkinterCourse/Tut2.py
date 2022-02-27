from tkinter import *

arpan_root=Tk()

# Width x Height
arpan_root.geometry("444x234")  #geometry means hum apni default window ka size set kar sakte hai

# width, height
arpan_root.minsize(300, 100)

# width, height
arpan_root.maxsize(1200,1000)

arpan1 = Label(text="Hello")    # Label -> wo hota hai jisse user interact nhi karta
arpan1.pack()

arpan_root.mainloop()