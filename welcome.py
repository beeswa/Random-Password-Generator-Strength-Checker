from tkinter import *
import os,sys
import random
from tkinter.font import Font
from tkinter.ttk import Combobox

def call_program():
  os.system('python main.py')

mainwindow = Tk()

mainwindow.title("Welcome to NHCE")
mainwindow.geometry("800x700+120+120")

subtitlefont=Font(size=15)

projecttitlefont=Font(family="Times New Roman", size=25, weight="bold", slant="italic", underline=1)

canvas = Canvas(width=500, height=150)
canvas.pack(padx=150)

photo = PhotoImage(file = '//root//Desktop//miniproject//nhce.png')

canvas.create_image(0,0, image=photo, anchor=NW)

titleframe = Frame(mainwindow)

subtitle = Label(titleframe, text = "Presents", font=subtitlefont)
subtitle.pack()

spacedivider = Label(titleframe, text="")
spacedivider.pack()

projecttitle = Label(titleframe, text = "Random Password Generator", font=projecttitlefont, fg="red")
projecttitle.pack()

projecttitle1 = Label(titleframe, text = "&", font=projecttitlefont, fg="red")
projecttitle1.pack()

projecttitle2 = Label(titleframe, text = "Strength Checker", font=projecttitlefont, fg="red")
projecttitle2.pack()

spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()

enterbutton = Button(titleframe, text="Get Started", width=15, height=2, font=subtitlefont, command=call_program)
enterbutton.pack()

spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()
spacedivider = Label(titleframe, text="")
spacedivider.pack()

titleframe.pack()

mainwindow.mainloop()
