from tkinter import *
from tkinter.ttk import *

screen=Tk()
screen.geometry("600x600")

cl=Label(screen,text="Coding Class Registration")
cl.place(x=190,y=10)

cor=Label(screen,text="Select your course")
cor.place(x=190,y=50)

cor1=StringVar()

combox=Combobox(screen,textvariable=cor1,width=25)
combox.place(x=140,y=90)
combox["values"]=["Coding","GUI","Python","Game Development"]


word=StringVar()

am10=Radiobutton(screen, text="Morning(10am)",variable=word,value=" Morning 10")
pm20=Radiobutton(screen, text="Evening(5pm)",variable=word,value=" Evening 5")

word.set(" Morning 10")
am10.place(x=320,y=150)
pm20.place(x=320,y=200)

def label():
    wrd=Label(screen,text="You have signed up for your class "+cor1.get()+" in the"+word.get())
    wrd.place(x=10,y=390)

enrb=Button(screen,text="Enroll Now",command=label)
enrb.place(x=230,y=260)

mainloop()