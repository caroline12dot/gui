from tkinter import *

screen=Tk()
screen.geometry("300x300")
spin=Spinbox(screen,from_=5,to=15)
spin.place(x=30,y=150)
mainloop()