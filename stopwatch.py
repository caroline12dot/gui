from tkinter import *
import time 
import tkinter.messagebox

screen=Tk()
screen.geometry("700x300")

def work():
    results=int(hour1.get())*3600+int(minute1.get())*60+int(second1.get())
    while results>-1:
        m,s=divmod(results,60)
        h=00
        if m>60:
            h,m=divmod(m,60)
        hour.set("{00:2d}".format(h))
        minute.set("{00:2d}".format(m))
        second.set("{00:2d}".format(s))

        screen.update()
        time.sleep(1)
        if results==0:
            tkinter.messagebox.showinfo("answer","Time up")
        results-=1   

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hour1=Entry(screen,textvariable=hour,width=2)
hour1.place(x=10,y=10)

minute1=Entry(screen,textvariable=minute,width=2)
minute1.place(x=55,y=10)

second1=Entry(screen,textvariable=second,width=2)
second1.place(x=90,y=10)

count=Button(screen,text="Start countdown",command=work)
count.place(x=250,y=150)

mainloop()