from tkinter import *
screen=Tk()
screen.geometry("700x200")

def convert():
    r=rentery.get()
    f=(float(r)/126.27)
    text.delete("1.0",END)
    text.insert(END,f)

rupees=Label(screen,text="Enter amount as rupees")
rupees.place(x=10,y=20)

rentery=Entry(screen)
rentery.place(x=360,y=20)

covert=Button(screen,text="Convert",command=convert)
covert.place(x=280,y=80)

text=Text(screen,height=1,width=20)
text.place(x=210,y=150)

mainloop()