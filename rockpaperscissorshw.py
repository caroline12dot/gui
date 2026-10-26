from tkinter import *
import random

screen=Tk()
screen.geometry("600x600")

def numchoice():
    number=random.randint(1,6)
    scr.config(text="Number is: "+str(number))

numb=Label(screen,text="Roll the Dice!")
numb.place(x=240,y=100)

nb=Button(screen,text="ROLL",command=numchoice)
nb.place(x=300,y=300)
scr=Label(screen,text="Number is: ")
scr.place(x=120,y=250)

mainloop()