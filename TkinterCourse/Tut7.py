from tkinter import *

root=Tk()
root.geometry("655x333")

def hello():
    print("Hello Arpan! How are you")

def joke():
    print("You Are")

def age():
    print("My age is 2 years")

def status():
    print("Good")

frame=Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

#command = (function ka naam aayega only function ki call nhi aayegi) jaise aapke function ka naam hai hello to only naam aayega hello means aap iss function ko direct execute kardo without calling or uski call nhi aayegi means hello() means hum usko call nhi karenge
b1=Button(frame, fg="red", text="Hello", command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame, fg="red", text="Tell me a joke", command=joke)
b2.pack(side=LEFT,padx=23)

b3=Button(frame, fg="red", text="Age", command=age)
b3.pack(side=LEFT,padx=23)

b4=Button(frame, fg="red", text="Status", command=status)
b4.pack(side=LEFT,padx=23)

root.mainloop()