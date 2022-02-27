from tkinter import *

root=Tk()

root.geometry("733x566")

root.title("PyCharm")

# def myfunc():
#     print("This is a function")

# Use these to create a non dropdown menu
# mymenu=Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

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


root.mainloop()