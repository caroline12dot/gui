from tkinter import *

screen=Tk()
screen.geometry("800x200")

def convertor():
    g=float(kg1.get())*1000
    p=float(kg1.get())*2.20462
    o=float(kg1.get())*35.274
    text1.delete("1.0",END)
    text1.insert(END,g)
    text2.delete("1.0",END)
    text2.insert(END,p)
    text3.delete("1.0",END)
    text3.insert(END,o)

kgs=Label(screen,text="Enter the weight in KG's")
kgs.place(x=10,y=10)

kg1=Entry(screen)
kg1.place(x=300,y=10)

convert=Button(screen,text="Convert",command=convertor)
convert.place(x=550,y=10)

grams=Label(screen,text="Grams")
grams.place(x=10,y=100)

text1=Text(screen,height=1,width=15)
text1.place(x=10,y=150)

pounds=Label(screen,text="Pounds")
pounds.place(x=250,y=100)

text2=Text(screen,height=1,width=15)
text2.place(x=250,y=150)

ounces=Label(screen,text="Ounces")
ounces.place(x=500,y=100)

text3=Text(screen,height=1,width=15)
text3.place(x=500,y=150)


mainloop()