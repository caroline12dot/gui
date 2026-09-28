from tkinter import *
from tkinter.ttk import*
import time

screen=Tk()
screen.geometry("900x700")

email=Label(screen,text="Email")
email.place(x=40,y=60)

emailbox=Entry(screen)
emailbox.place(x=150,y=60)

password=Label(screen,text="Password")
password.place(x=40,y=150)

passbox=Entry(screen,show="*")
passbox.place(x=150,y=150)

what=Label(screen,text="what food would you like: chicken sandwich, veg sandwich or none")
what.place(x=40,y=250)

wat=Entry(screen)
wat.place(x=40,y=300)

spin=Spinbox(screen,from_=5,to=15)
spin.place(x=300,y=300)

bev=Label(screen,text="what beverages would you like: water, fanta, water or none")
bev.place(x=40,y=380)

beve=Entry(screen)
beve.place(x=40,y=430)

spin1=Spinbox(screen,from_=5,to=15)
spin1.place(x=300,y=430)

desert=Label(screen,text="what desert would you like: ice cream, ice lolly, chocolate cake or none")
desert.place(x=40,y=500)

des=Entry(screen)
des.place(x=40,y=550)

spin2=Spinbox(screen,from_=5,to=15)
spin2.place(x=300,y=550)


progress=Progressbar(screen,orient=HORIZONTAL,length=250)
def prog():
    progress["value"]=20
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=60
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=80
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=100
    screen.update_idletasks()
    time.sleep(1)
progress.place(x=350,y=650)

button1=Button(screen,text="Submit Order",command=prog)
button1.place(x=400,y=600)


mainloop()
