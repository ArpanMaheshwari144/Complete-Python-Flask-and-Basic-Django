from tkinter import *

import tkinter.messagebox as tmsg

root=Tk()

root.geometry("733x566")

root.title("PyCharm")

def myfunc1():
    print("Creates new project")

def myfunc2():
    print("Creates new file")

def myfunc3():
    print("Save file")

def myfunc4():
    print("Seve as file")

def myfunc5():
    print("Open project")

def myfunc6():
    print("Close project")

def myfunc7():
    print("Print")

def myfunc8():
    print("Cut")

def myfunc9():
    print("Copy")

def myfunc10():
    print("Paste")

def myfunc11():
    print("Delete")

def myfunc12():
    print("Select All Files")

def myfunc13():
    print("Sort Lines")

def myfunc14():
    print("Reverse Lines")

def help():
    print("I will help you")

    tmsg.showinfo("Help", "Arpan will help you")
             #or
    # a=tmsg.showinfo("Help", "Arpan will help you")
    # print(a)

def rate():
    print("Rate Us")

    # tmsg.askquestion("How's Your Experience?", "Was Your Experience Good?")
                     #or
    value=tmsg.askquestion("How's Your Experience?", "Was Your Experience Good?")
    print(value)

    if value=="yes":
        msg="Great. Rate us on appstore please"
    else:
        msg="Tell us what went wrong"
    tmsg.showinfo("How's Your Experience?", msg)

def divya():
    ans=tmsg.askretrycancel("Divya se dostikarlo", "Divya dost nhi banegi")
    if ans:
        print("Retry karne se bhi kuch nhi hoga")
    else:
        print("Bdiya bhia retry kar diya")

mainmenu=Menu(root)   # maimenu = menubar

# m1=Menu(mainmenu)       # m1 is the option of mainmenu
m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc1)
m1.add_command(label="New", command=myfunc2)
m1.add_command(label="Save", command=myfunc3)
m1.add_command(label="Save As", command=myfunc4)
m1.add_separator()
m1.add_command(label="Open Project", command=myfunc5)
m1.add_command(label="Close Project", command=myfunc6)
m1.add_command(label="Print", command=myfunc7)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)

# m2=Menu(mainmenu)     # m2 is the another option of mainmenu
m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc8)
m2.add_command(label="Copy", command=myfunc9)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc10)
m2.add_command(label="Delete", command=myfunc11)
m2.add_separator()
m2.add_command(label="Select All", command=myfunc12)
m2.add_command(label="Sort Lines", command=myfunc13)
m2.add_command(label="Reverse Lines", command=myfunc14)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)

# m3=Menu(mainmenu)   # m3 is the another option of mainmenu
m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="BeFriendDivya", command=divya)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

root.mainloop()
