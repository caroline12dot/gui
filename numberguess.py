from tkinter import *
import random
import tkinter.messagebox

screen=Tk()
screen.geometry("400x400")

def okmessege():
    name=ne1.get()
    tkinter.messagebox.showinfo("name","Hello "+str(name)+" I am thinking of a number between 1&20")


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
gb=Button(screen,text="Guess")
gb.place(x=280,y=330)

mainloop()