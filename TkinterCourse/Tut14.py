from tkinter import *

def getvals():
    print(f"{fnamevalue.get(),lnamevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")   # this will return a tuple

    with open("Travelrecords.txt", "a") as f:
        f.write(f"{fnamevalue.get(),lnamevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")

root=Tk()

root.geometry("600x300")

# heading
Label(root, text="Welcone to Arpan's Travel", font="comicsansms 13 bold", pady=15).grid(row=0,column=3)

# Text for our form
fname=Label(root, text="FirstName")
lname=Label(root, text="LastName")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency Contact")
paymentmode=Label(root, text="Payment Mode")

# Pack text for our form
fname.grid(row=1,column=2)
lname.grid(row=2,column=2)
phone.grid(row=3,column=2)
gender.grid(row=4,column=2)
emergency.grid(row=5,column=2)
paymentmode.grid(row=6,column=2)

# tkinter variable for storing entries
fnamevalue=StringVar()
lnamevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# Entries for our form
fnameentry=Entry(root, textvariable=fnamevalue)
lnameentry=Entry(root, textvariable=lnamevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

# Pack entries for our form
fnameentry.grid(row=1,column=3)
lnameentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
emergencyentry.grid(row=5,column=3)
paymentmodeentry.grid(row=6,column=3)

# Adding Checkbox
foodservice=Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)

#Pack Checkbox
foodservice.grid(row=7, column=3)

# Adding Button and command
Button(text="Submit", command=getvals).grid(row=8,column=3)

root.mainloop()