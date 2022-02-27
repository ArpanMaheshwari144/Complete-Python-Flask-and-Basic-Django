from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")

root.title("Arpan's GUI")

canvas_widget=Canvas(root, width=canvas_width, height=canvas_height)

canvas_widget.pack()

# The line goes from x1, y1 to x2, y2
# canvas_widget.create_line(0, 0, 800, 400, fill="red")
# canvas_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - co-ordinates of top left and co-ordinates of bottom right
canvas_widget.create_rectangle(3, 5, 700, 300, fill="purple")

# create_text ke co-ordinates (x,y,text="")
canvas_widget.create_text(400,200, text="Arpan Maheshwari")

canvas_widget.create_oval(444, 133, 344, 355)


root.mainloop()