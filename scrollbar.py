from tkinter import *

screen=Tk()
screen.geometry("700x700")

bar=Scrollbar(screen)
bar.pack(side=RIGHT,fill=Y)
list1=Listbox(screen,yscrollcommand=bar.set)
for i in range(100):
    list1.insert(END,i)
list1.pack(side=LEFT,fill=BOTH)
bar.config(command=list1.yview)

mainloop()