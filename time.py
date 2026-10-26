from tkinter import *
from time import strftime

screen=Tk()
screen.geometry("500x200")

def time():
    time1=strftime("%H:%M:%S %p")
    time2=Label(screen,font=("Calibri",45))
    time2.config(text=time1)
    time2.after(1000,time)
    time2.place(x=10,y=100)
time()

mainloop()
