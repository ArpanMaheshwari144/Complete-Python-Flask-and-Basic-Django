from tkinter import *

def submit():
    print("Values has been submitted")
root=Tk()

root.geometry("633x344")

user=Label(root, text="Username").grid(padx=5,pady=5)
password=Label(root, text="Password").grid(padx=5,pady=5)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue).grid(row=0,column=1)
passentry=Entry(root, textvariable=passvalue).grid(row=1,column=1)

Button(text="Submit", command=submit).grid()

root.mainloop()