from tkinter import *

def submit():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

root=Tk()
root.geometry("655x333")

user=Label(root, text="Username")
password=Label(root, text="Password")

# .grid function 2 arguments leta hai:(or by default ye row=0 or column=0 leta hai)
# 1. row
# 2. column
user.grid()   #.grid ek function hota hai tkinter mei pack karne ke liye
password.grid()

#Variables classes in tkinter:BooleanVar, DoubleVar, IntVar, StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

# Making of button in one line
Button(text="Submit", command=submit).grid()


root.mainloop()

