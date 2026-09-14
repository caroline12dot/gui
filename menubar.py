from tkinter import *
from tkinter.ttk import*

screen=Tk()
screen.geometry("900x700")

menubar=Menu(screen)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New File")
file.add_command(label="Open")
file.add_command(label="Delete")
file.add_separator()
file.add_command(label="Exit",command=screen.destroy)

edit=Menu(menubar)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Image")
edit.add_command(label="Text")
edit.add_command(label="Videos")
edit.add_separator()
edit.add_command(label="Undo")
screen.config(menu=menubar)



mainloop()
