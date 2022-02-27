from tkinter import *

def button1(event):
    print(f"You just clicked the button at {event.x}, {event.y}")   # agar aap window ko shift karte rahenge to x and y co-ordinates ki values bhi change hoti rahengi

root=Tk()

root.title("Events")

root.geometry("644x344")

widget=Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>',  button1)
widget.bind('<Double-1>',  quit)


root.mainloop()