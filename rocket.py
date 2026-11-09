from tkinter import *
import time 
import tkinter.messagebox

screen=Tk()
screen.geometry("700x300")

def work():
        global timeleft
        timer.config(text=str(timeleft))
        if timeleft>5:
              status.config(text="engine start")
        elif timeleft>0:
              status.config(text="ignition sequence")
        else:
              status.config(text="blast off")
              return
        timeleft-=1
        screen.after(1000,work)

def launch():
       global timeleft
       timeleft=10
       work()

timer=Label(screen, text="10")
timer.place(x=350,y=10)

status=Label(screen,text="Preparing")
status.place(x=350,y=100)

count=Button(screen,text="Launch Rocket",command=launch)
count.place(x=250,y=150)

mainloop()