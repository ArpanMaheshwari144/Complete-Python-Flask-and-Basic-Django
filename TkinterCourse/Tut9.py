import tkinter as tk

def write_message():
    print("https://google.com/")
def name():
    print("My Name Is Arpan Maheshwari")
def message():
    print("Hello friends chai peelo")
def lmessage():
    print("Bharat Mata Ki Jay!")
def b5():
    print("I love my country")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
#Button1
button = tk.Button(frame,
                   text="Apan ka Naam",
                   fg="red",
                   command=name)
button.pack(side=tk.LEFT)
#Button 2
Website = tk.Button(frame,
                   text="Google",
                   command=write_message)
Website.pack(side=tk.LEFT)
#Button 3
click= tk.Button(frame,
                 text="Isko Dabao Dekho Message Milega",
                 command=message)
click.pack(side=tk.LEFT)
#Button 4
lm= tk.Button(frame,
              text="Isko Daba Daala To Life Jhingalala",
              command=lmessage)
lm.pack(side=tk.LEFT)
#Button 5
b5=tk.Button(frame,
             text="Ab Mujhe Bhi Daba Do!",
             command=b5)
b5.pack(side=tk.LEFT)
root.mainloop()