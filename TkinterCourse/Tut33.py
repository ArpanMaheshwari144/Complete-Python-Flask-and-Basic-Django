from tkinter import *

root=Tk()

root.geometry("655x444")

root.title("Arpan's GUI")

root.wm_iconbitmap("notepad.ico")
root.configure(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()


root.mainloop()