from tkinter import *

root = Tk()
root.title("Exercise1")
root.geometry("500x400")

label = Label(text = "Ready !!" ,bg= "white",padx = 50)
label.pack(side = BOTTOM, fill = X)

#Frame
f1= Frame(root, bg= "grey")
f1.pack(side = TOP,fill=X)

name = Label(f1,text = "Welcome to Scorpion !",bg = "grey",padx = 50 ,fg = "white", font = "arial 10 bold")
name.pack()

def button1():
    print("Button 1 pressed !")
def button2():
    print("Button 2 pressed !")
def button3():
    print("Button 3 pressed !")
def button4():
    print("Button 4 pressed !")

frame = Frame(root, bg= "grey")
frame.pack(side = LEFT , fill = Y)

b1 = Button(frame ,text = "1",padx= 25 , pady = 25,command = button1)
b1.pack(fill = X)

b2 = Button(frame ,text = "2",padx= 25 , pady = 25,command = button2)
b2.pack(fill = X)

b3 = Button(frame ,text = "3",padx= 25 , pady = 25,command = button3)
b3.pack(fill = X)

b4 = Button(frame ,text = "4",padx= 25 , pady = 25,command = button4)
b4.pack(fill = X)

root.mainloop()