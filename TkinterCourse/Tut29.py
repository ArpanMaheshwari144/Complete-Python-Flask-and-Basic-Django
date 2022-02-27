from tkinter import *
import tkinter.messagebox as tmsg


def myfunc():
    print("it is a text editor program")


def Quit():
    window.destroy()


def help():
    a = tmsg.showinfo("Help", "Arpan will help u in this GUI")


# def feed():
#  print("Give us yout Valuable Feedback")


window = Tk()
window.geometry("920x680")
window.title("New Text Document- Notepad")
window.configure(bg="white", borderwidth=2)
mainmenu = Menu(window)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New                 Ctrl+N", command=myfunc)
m1.add_command(label="New Window          Ctrl+Shift+N", command=myfunc)
m1.add_command(label="Open...             Ctrl+O", command=myfunc)
m1.add_command(label="Save                Ctrl+S", command=myfunc)
m1.add_command(label="Save As...         Ctrl+Shift+S", command=myfunc)
m1.add_separator(0)
m1.add_command(label="Page Setup...", command=myfunc)
m1.add_command(label="Print...            Ctrl+P", command=myfunc)
m1.add_separator(0)
m1.add_command(label="Exit", command=Quit)

window.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo              Ctrl+Z", command=myfunc)
m2.add_separator(0)
m2.add_command(label="Cut               Ctrl+X", command=myfunc)
m2.add_command(label="Copy              Ctrl+C", command=myfunc)
m2.add_command(label="Paste             Ctrl+V", command=myfunc)
m2.add_command(label="Delete            Del", command=myfunc)
m2.add_separator(0)
m2.add_command(label="Page Setup...", command=myfunc)
m2.add_command(label="Print...            Ctrl+P", command=myfunc)
m2.add_separator(0)
m2.add_command(label="Search With Bing... Ctrl+E", command=myfunc)
m2.add_command(label="Find...              Ctrl+F", command=myfunc)
m2.add_command(label="Find Next             F3", command=myfunc)
m2.add_command(label="Find Previous         Shift+F3", command=myfunc)
m2.add_command(label="Replace               Ctrl+H", command=myfunc)
m2.add_command(label="Go To...              Ctrl+G", command=myfunc)
m2.add_separator(0)
m2.add_command(label="Select All            Ctrl+A", command=myfunc)
m2.add_command(label="Time\Date             F5", command=myfunc)
window.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Word Wrap", command=myfunc)
m3.add_command(label="Font", command=myfunc)
window.config(menu=mainmenu)
mainmenu.add_cascade(label="Format", menu=m3)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Zoom", command=myfunc)
m4.add_command(label="Status Bar", command=myfunc)
window.config(menu=mainmenu)
mainmenu.add_cascade(label="View", menu=m4)

m5 = Menu(mainmenu, tearoff=0)
m5.add_command(label="View Help", command=help)
m5.add_command(label="Send Feedback", command=myfunc)
m5.add_separator(0)
m5.add_command(label="About Notepad")
window.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m5)

# to add ascroll bar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(window, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

window.mainloop()