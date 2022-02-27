from tkinter import *

def getvals():
    print(namevalue.get())
    print(phonevalue.get())
    print(gendervalue.get())
    print(emergencyvalue.get())
    print(paymentmodevalue.get())

root=Tk()

root.geometry("600x300")

# heading
Label(root, text="Welcone to Arpan's Travel", font="comicsansms 13 bold", pady=15).grid(row=0,column=3)

# Text for our form
name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency Contact")
paymentmode=Label(root, text="Payment Mode")

# Pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# Entries for our form
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

# Pack entries for our form
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# Adding Checkbox
foodservice=Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)

#Pack Checkbox
foodservice.grid(row=6, column=3)

# Adding Button and command
Button(text="Submit", command=getvals).grid(row=7,column=3)

root.mainloop()