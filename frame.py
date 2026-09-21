from tkinter import *

screen=Tk()
screen.geometry("700x700")

frame1=Frame(screen,bg="Pink",width=400,height=300)
frame1.pack()

frame2=Frame(screen,bg="Purple",width=300,height=400)
frame2.pack(side=BOTTOM)

b1=Button(frame1,text="okay")
b1.pack(side=LEFT)

b2=Button(frame1,text="ok")
b2.pack(side=LEFT)

b3=Button(frame1,text="hello")
b3.pack(side=LEFT)

b4=Button(frame2,text="hi")
b4.pack(side=BOTTOM)

b5=Button(frame2,text="hey")
b5.pack(side=BOTTOM)

b6=Button(frame2,text="okay")
b6.pack(side=BOTTOM)

mainloop()
