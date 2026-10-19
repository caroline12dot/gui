from tkinter import *
import random

screen=Tk()
screen.geometry("1000x600")

playerscore=0
computerscore=0
options=[("rock",0),("paper",1),("scissors",2)]

def computerwin():
    global computerscore,playerscore
    computerscore+=1
    win.config(text="Computer wins")
    comps.config(text="Computer score: "+str(computerscore))
    playrs.config(text="Your score: "+str(playerscore))

def playerwin():
    global playerscore,computerscore
    playerscore+=1
    win.config(text="You win")
    playrs.config(text="Your score: "+str(playerscore))
    comps.config(text="Computer score: "+str(computerscore))

def tie():
    global playerscore,computerscore
    win.config(text="Tie")
    playrs.config(text="Your score: "+str(playerscore))
    comps.config(text="Computer score: "+str(computerscore))

def computerchoice():
    return random.choice(options)

def playerchoice(playerinput):
    global playerscore,computerscore
    computerinput=computerchoice()
    comutr.config(text="Computer selected: "+computerinput[0])
    playr.config(text="You selected: "+playerinput[0])
    if playerinput==computerinput:
        tie()
    elif playerinput[1]==0:
        if computerinput[1]==1:
            computerwin()
        elif computerinput[1]==2:
            playerwin()
    elif playerinput[1]==1:
        if computerinput[1]==0:
            playerwin()
        elif computerinput[1]==2:
            computerwin()
    elif playerinput[1]==2:
        if computerinput[1]==0:
            computerwin()
        elif computerinput[1]==2:
            playerwin()
       

rps=Label(screen,text="Rock,Paper,Scissors")
rps.place(x=410,y=40)

win=Label(screen,text="Lets start the game",fg="Red")
win.place(x=410,y=100)

option=Label(screen,text="Your options")
option.place(x=220,y=150)

rockb=Button(screen,text="Rock",command=lambda:playerchoice(options[0]))
rockb.place(x=350,y=180)

scissorsb=Button(screen,text="Scissors",command=lambda:playerchoice(options[2]))
scissorsb.place(x=470,y=180)

paperb=Button(screen,text="Paper",command=lambda:playerchoice(options[1]))
paperb.place(x=630,y=180)

scr=Label(screen,text="Score")
scr.place(x=220,y=250)

playr=Label(screen,text="You selected")
playr.place(x=350,y=280)

comutr=Label(screen,text="Computer selected")
comutr.place(x=350,y=360)

playrs=Label(screen,text="Your score")
playrs.place(x=680,y=280)

comps=Label(screen,text="Computer score")
comps.place(x=680,y=360)



mainloop()