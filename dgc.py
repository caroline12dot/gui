from tkinter import *
from time import strftime

screen=Tk()
screen.geometry("1000x200")

cw=Label(screen,text="Calender Widget")
cw.place(x=10,y=10)

def time():
    time1=strftime("%B %d,%Y")
    time2=Label(screen,font=("Calibri",35))
    time2.config(text=time1)
    time2.after(1000,time)
    time2.place(x=10,y=100)
time()

mainloop()
