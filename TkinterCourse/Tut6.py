from tkinter import *
root=Tk()
root.geometry("655x333")

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=142)

l2=Label(f2,text="Welcome to my project",font="Helvetica 16 bold",fg="red",pady=20)
l2.pack()

root.mainloop()