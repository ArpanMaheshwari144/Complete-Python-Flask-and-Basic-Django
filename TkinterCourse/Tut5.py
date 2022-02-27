from tkinter import *
root = Tk()
root.geometry("744x433")
root.title("Arpan Maheshwari")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground(text ka color)
# font - sets the font:
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and television personality.In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting.He has a significant following in Asia and the Indian \ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian \ncinema.According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was \nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''', bg ="red", fg="white", padx=34, pady=34, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor =  nw(northwest)
# side = top, bottom, left, right
# fill=X/"x" (X means jab hum window ko X-axis ki taraf le kar jayenge to ye X-aixis mei expand hoga)
# fill=Y/"y" (Y means jab hum window ko Y-axis ki taraf le kar jayenge to ye Y-aixis mei expand hoga)
# padx
# pady

# title_label.pack(anchor="nw")
# title_label.pack(anchor="ne")
# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


