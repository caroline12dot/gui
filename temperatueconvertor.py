from tkinter import *
screen=Tk()
screen.geometry("700x200")

def convert():
    c=centery.get()
    f=(float(c)*9/5)+32
    text.delete("1.0",END)
    text.insert(END,f)

celcius=Label(screen,text="Enter temperature as celius")
celcius.place(x=10,y=20)

centery=Entry(screen)
centery.place(x=360,y=20)

covert=Button(screen,text="Convert",command=convert)
covert.place(x=280,y=80)

text=Text(screen,height=1,width=20)
text.place(x=210,y=150)

mainloop()