from tkinter import *
from tkinter.ttk import*
import time

screen=Tk()
screen.geometry("900x700")

progress=Progressbar(screen,orient=VERTICAL,length=100)

def bar():
    progress["value"]=10
    screen.update_idletasks() 
    time.sleep(1)
    progress["value"]=20
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=30
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=50
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=60
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=80
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=100
progress.place(x=200,y=200)
button=Button(screen,text="Start",command=bar)
button.place(x=360,y=200)
mainloop()
    