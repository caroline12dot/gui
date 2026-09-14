from tkinter import *

screen=Tk()

screen.title("Book inventory")
screen.geometry("900x700")
screen.config(background="pink")

title=Label(screen,text="Title")
title.place(x=40,y=60)

author=Label(screen,text="Author")
author.place(x=40,y=150)

price=Label(screen,text="Price")
price.place(x=40,y=210)

titlebox=Entry(screen)
titlebox.place(x=120,y=60)

authorbox=Entry(screen)
authorbox.place(x=120,y=150)

pricebox=Entry(screen)
pricebox.place(x=120,y=210)

button=Button(screen,text="Submit",command=screen.destroy)
button.place(x=480,y=360)

mainloop()