from tkinter import *
from tkinter.ttk import *

screen=Tk()
screen.geometry("600x600")

multi=Label(screen,text="Mathematical Table")
multi.place(x=230,y=10)

num=Label(screen,text="Number and Range:")
num.place(x=20,y=70)

num1=IntVar()

combox=Combobox(screen,textvariable=num1,width=3)
combox.place(x=250,y=70)
combox["values"]=list(range(16))

rad=IntVar()

r10=Radiobutton(screen, text="10",variable=rad,value=10)
r20=Radiobutton(screen, text="20",variable=rad,value=20)
r30=Radiobutton(screen, text="30",variable=rad, value=30)
rad.set(10)
r10.place(x=320,y=70)
r20.place(x=320,y=110)
r30.place(x=320,y=150)

def table():
    wholetab=""
    for i in range(rad.get()+1):
        wholetab+=str(num1.get())+" x "+str(i)+" = "+str(num1.get()*i)+"\n"
    Tab1=Label(screen,text="Multiplication table for "+wholetab)
    Tab1.place(x=15,y=240)
button1=Button(screen,text="Generate Now",command=table)
button1.place(x=270,y=195)

mainloop()
