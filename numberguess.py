from tkinter import *
import random
import tkinter.messagebox

screen=Tk()
screen.geometry("400x400")
choice=random.randint(1,20)

def okmessege():
    name=ne1.get()
    tkinter.messagebox.showinfo("name","Hello "+str(name)+" I am thinking of a number between 1&20")

def numberg():
    number=n1.get()
    number=int(number)
    if number<choice:
        tkinter.messagebox.showerror("low","The number you guessed is too low")
    elif number>choice:
        tkinter.messagebox.showerror("high","The number you guessed is too high")
    elif number==choice:
        tkinter.messagebox.showinfo("right","Well done that is the correct guess") 


welcome=Label(screen,text="Welcome to the number guess game")
welcome.place(x=10,y=40)

name1=Label(screen,text="What is your name?")
name1.place(x=20,y=140)
ne1=Entry(screen)
ne1.place(x=20,y=180)
ob=Button(screen,text="Okay",command=okmessege)
ob.place(x=280,y=180)

num=Label(screen,text="What is the number?")
num.place(x=20,y=270)
n1=Entry(screen)
n1.place(x=20,y=330)
gb=Button(screen,text="Guess",command=numberg)
gb.place(x=280,y=330)

mainloop()