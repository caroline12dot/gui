from tkinter import *

screen=Tk()

screen.title("Login")
screen.geometry("970x690")
screen.config(background="purple")

username=Label(screen,text="Username")
username.place(x=40,y=60)

password=Label(screen,text="Password")
password.place(x=40,y=150)

userbox=Entry(screen)
userbox.place(x=250,y=60)

passbox=Entry(screen,show="$")
passbox.place(x=250,y=150)

button=Button(screen,text="Submit",command=screen.destroy)
button.place(x=480,y=360)


mainloop()