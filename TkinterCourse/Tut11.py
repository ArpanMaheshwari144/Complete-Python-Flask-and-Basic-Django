from tkinter import  *

def getvals():
    print(f"The value of user is {fnamevalue.get()}")
    print(f"The value of user password is {lnamevalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{fnamevalue.get(), lnamevalue.get()}\n")  # this will return a tuple


root=Tk()

root.geometry("500x400")

Label(root, text="Dance Club", fg = "green", font = "verdana 20 bold", padx=10).grid()
fname = Label(root, text = "First Name")
lname = Label(root, text = "Last Name")
fname.grid()
lname.grid()

fnamevalue=StringVar()
lnamevalue=StringVar()

fnameentry=Entry(root, textvariable=fnamevalue)
lnameentry=Entry(root, textvariable=lnamevalue)
fnameentry.grid(row=1, column=1)
lnameentry.grid(row=2, column=1)

Button(text = "Submit", bg = "grey", pady = 5, command = getvals).grid()

root.mainloop()

