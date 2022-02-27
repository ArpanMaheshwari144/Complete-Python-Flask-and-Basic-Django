from tkinter import *

root=Tk()

root.geometry("455x233")

root.title("Sliders")

def rate():
    with open("rating.txt", "a") as f:
        f.write(f"App got rating of {rating.get()} stars\n")
    print(f"User give rating of {rating.get()} stars ")

rating=Scale(root ,from_=0, to=10, orient=HORIZONTAL, tickinterval=3, width=6)
rating.pack()

Button(root, text="Submit", command=rate).pack()

root.mainloop()