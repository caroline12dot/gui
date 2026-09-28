from tkinter import *
import calendar

screen=Tk()
screen.geometry("900x900")

def displaycal():
    screen2=Tk()
    screen2.geometry("1000x1500")
    year=int(entb1.get())
    content=calendar.calendar(year)
    cal=Label(screen2,text=content)
    cal.place(x=10,y=10)


cal1=Label(screen,text="Calendar",font=("Calibri",25))
cal1.place(x=350,y=100)

entyr=Label(screen,text="Enter year")
entyr.place(x=380,y=200)

entb1=Entry(screen)
entb1.place(x=320,y=250)

butc1=Button(screen,text="Show calendar",command=displaycal)
butc1.place(x=350,y=290)

exibuto=Button(screen,text="Exit",command=exit)
exibuto.place(x=400,y=345)


mainloop()