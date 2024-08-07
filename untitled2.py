# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:25:28 2024

@author: occup
"""

from tkinter import *
import random
root = Tk()
root.geometry("600x600")

label_colors = Label(root)

 
root.geometry("600x600")

rand_colors = { "colors" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"], }
def back_color():
   rand_color = random.randint(0,7)
   color = rand_colors["colors"] + [rand_color]
   print("color")



btn_color = Button(root, text = "rand color", command = back_color)
btn_color.place(relx = 0.5, rely = 0.2, anchor = CENTER)








label_colors.place(relx = 0.5, rely = 0.3, anchor = CENTER)
root.configure(background = "color")
root.mainloop()
