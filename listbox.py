from tkinter import *

screen=Tk()
screen.geometry("700x700")

list1=Listbox(screen,width=40,height=20,bg="pink")
list1.insert(1,"hello")
list1.insert(2,"hi")
list1.insert(3,"greetings")
list1.pack()

mainloop()