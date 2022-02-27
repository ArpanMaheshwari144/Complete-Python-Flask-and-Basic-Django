from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")

root.title("Arpan's GUI")

canvas_widget=Canvas(root, width=canvas_width, height=canvas_height)

canvas_widget.pack()
canvas_widget.create_arc(200,200,577,444)

photo=PhotoImage(file="social.png")
canvas_widget.create_image(10,10,image=photo)
canvas_widget.create_bitmap(355,53,bitmap='error')
canvas_widget.create_bitmap(400,60,bitmap='hourglass')
canvas_widget.create_bitmap(455,65,bitmap='info')
canvas_widget.create_bitmap(500,70,bitmap='question')
canvas_widget.create_bitmap(555,80,bitmap='warning')

root.mainloop()