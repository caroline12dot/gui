from tkinter import *
import random

screen=Tk()
screen.geometry("1000x600")
options=["blue","green","purple","red","orange","yellow"]

def colourchoice():
    colour=random.choice(options)
    screen.config(bg=colour)
    scr.config(text="Colour is: "+str(colour))

color=Label(screen,text="Colour Magic")
color.place(x=10,y=40)

cb=Button(screen,text="Change Colour",command=colourchoice)
cb.place(x=630,y=180)
scr=Label(screen,text="Colour is: ")
scr.place(x=220,y=250)

mainloop()