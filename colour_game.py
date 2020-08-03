from tkinter import *
from PIL import Image,ImageTk
import random
import time
import sqlite3
connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

score=0
timer=0
def destructColourGame(window,val):
    global ID
    ID=val    
    ColourGUI()

def new_game():
    global timer
    if timer==30:
        count()
    enter()

def exit():
    global score
    global ID
    global c
    tt=Tk()
    tt.title("Scoreboard")
    p=Label(tt,text="Time over so game ended!",font="Signboard 24 bold underline")
    l=Label(tt,text="GAME OVER! YOUR SCORE IS :",font="Signboard 22 bold underline")
    l.pack()
    l1=Label(tt,text=score,font="Signboard 22 bold")
    l1.pack()
    sql="SELECT COLOUR FROM SCORE WHERE ID=?"
    cursor.execute(sql,[(ID)])
    val=cursor.fetchone()
    if val==None:
        val2=0
    else:
        val2=val[0]
    val3=val2+score
    sql2="UPDATE SCORE SET COLOUR=? WHERE ID=?"
    cursor.execute(sql2,[val3,(ID)])
    connection.commit()

    cursor.execute("SELECT MAX(COLOUR) FROM SCORE")
    val=cursor.fetchone()
    val1=val[0]
    str2="HIGH SCORE: "+str(val1)
    str3="YOUR PREVIOUS SCORE: "+str(val2)
    str4="YOUR CURRENT SCORE: "+str(val3)
    l3=Label(tt,text=str2,font="Signboard 22 bold")
    l4=Label(tt,text=str3,font="Signboard 22 bold")
    l5=Label(tt,text=str4,font="Signboard 22 bold")
    l3.pack()
    l4.pack()
    l5.pack()
    c.destroy()
        
    b1=Button(tt,text="QUIT?",font="Signboard 20 bold",bg="white",fg="black",command=tt.destroy)
    b1.pack()
    tt.mainloop()
def enter():
    global c
    global e1
    global score
    global timer
    global colours
    global lab
    global sc1
    
    if timer>0:
        e1.focus_set()
        if e1.get().lower()==colours[1].lower():
            score=score+1
        random.shuffle(colours)
        lab.config(fg=str(colours[1]),text=str(colours[0]))
        sc1.config(text=str(score))
def count():
    global timer
    global timing1
    if timer>0:
        timer=timer-1
        timing1.config(text=str(timer))
        timing1.after(1000,count)
    else:
        exit()
        
def ColourGUI():
    global c
    global e1
    global colours
    global score
    global timer
    global lab,sc1,timing1

    c=Toplevel()
    colours=["Red","Blue","Green","Pink","Black","Yellow","Orange","Brown","Purple",]
    timer=30

    c.title("Colour Game")
    c.geometry("800x500")
    c.configure(bg="bisque")
    l1=Label(c,text="WELCOME TO THE COLOUR GAME",font="Verdana 30 bold italic",fg="skyblue",bg="black")
    l1.place(x=300,y=100)

    l2=Label(c,text="Type the colour of the word,",font="Helvetica 30 italic",fg="red",bg="bisque")
    l2.place(x=450,y=250)
    l3=Label(c,text="and not the word text itself!",font="Helvetica 30 italic",fg="red",bg="bisque")
    l3.place(x=450,y=300)

    l4=Label(c,text="Click ENTER to Start the timer",font="Verdana 30 bold",fg="black",bg="bisque")
    l4.place(x=400,y=450)

    timing=Label(c,text="Time Left->",font="Stencil 25 bold underline",fg="black",bg="bisque")
    timing.place(x=1000,y=50)
    
    timing1=Label(c,text=timer,font="Stencil 25 bold",fg="black",bg="bisque")
    timing1.place(x=1200,y=50)

    sc=Label(c,text="Score->",font="Stencil 25 bold underline",fg="black",bg="bisque")
    sc.place(x=70,y=50)
    sc1=Label(c,text=score,font="Stencil 25 bold",fg="black",bg="bisque")
    sc1.place(x=200,y=50)

    lab=Label(c,text=str(colours[0]),fg=str(colours[1]),font="Baskerville 35 bold")
    lab.place(x=650,y=550)
    
    e1=Entry(c,font="Baskrerville 20")
    e1.place(x=600,y=650)
    e1.focus_set()

    sub=Button(c,text=" Enter ",font="Verdana 25",command=new_game)
    sub.place(x=650,y=700)

    c.mainloop()

    
    
