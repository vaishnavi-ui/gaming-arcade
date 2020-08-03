#importing pygame
import pygame

from tkinter import *
#importing pillow(image border)
from PIL import Image,ImageTk,ImageOps

from tkinter import messagebox
import string
import sqlite3
connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

score=0
number=0
def destructLogoGame(window,val):
    global ID
    ID=val    
    logogameGUI()

def exit():
    global score
    global ID
    global t

    e=Tk()
    l=Label(e,text="GAME OVER! YOUR SCORE IS :",font="Signboard 22 bold underline")
    l.pack()
    l1=Label(e,text=score,font="Signboard 22 bold")
    l1.pack()
    sql="SELECT GTL FROM SCORE WHERE ID=?"
    cursor.execute(sql,[(ID)])
    val=cursor.fetchone()
    if val==None:
        val2=0
    else:
        val2=val[0]
    val3=val2+score
    sql2="UPDATE SCORE SET GTL=? WHERE ID=?"
    cursor.execute(sql2,[val3,(ID)])
    connection.commit()

    cursor.execute("SELECT MAX(GTL) FROM SCORE")
    val=cursor.fetchone()
    val1=val[0]
    str2="HIGH SCORE: "+str(val1)
    str3="YOUR PREVIOUS SCORE: "+str(val2)
    str4="YOUR CURRENT SCORE: "+str(val3)
    l3=Label(e,text=str2,font="Signboard 22 bold")
    l4=Label(e,text=str3,font="Signboard 22 bold")
    l5=Label(e,text=str4,font="Signboard 22 bold")
    l3.pack()
    l4.pack()
    l5.pack()
    t.destroy()
        
    b1=Button(e,text="QUIT?",font="Signboard 20 bold",bg="white",fg="black",command=e.destroy)
    b1.pack()
    e.mainloop()
    
   
#Hint Function
def hint():
    hint=Tk()
    hint.title("Hint option")
    hint.geometry("200x200")
    hintLabel=Label(hint,text="You have chosen the hint option!")
    hintLabel.pack()

    
#Score function
def Score():
    #Displaying score
    scoreText=" Score: "+str(score)
    scoreLabel=Label(t,text=scoreText,font="Bodoni 20 bold italic",bd=4,bg="white",fg="blue")#try and give a border colour to this label
    scoreLabel.grid(row=1,column=3)

def new_game():
    global t
    global number
    global pics
    global names
    
    #placing image on window
    img=Label(t,image=pics[number])
    img.place(x=500,y=200)
    img.config(image=pics[number])

    #displaying Score
    ls=Label(t,text="Score ->",font="Stencil 20",fg="black")
    ls.place(x=1200,y=50)
    lss=Label(t,text=score,font="Stencil 20",fg="black")
    lss.place(x=1300,y=50)
    

#checking the logo
def checkLogo():
    global score
    global number
    global names
    global e1
    global t

    if(e1.get()==names[number]):
        messagebox.showinfo("game","CORRECT ANSWER")
        score=score+1
        number=number+1
        new_game()
    else:
        
        messagebox.showwarning("game","WRONG ANSWER")
        exit()
        

def logogameGUI():
    global t
    global score
    global pics
    global names
    global number
    global e1
 
    t=Toplevel()

    pics=[ImageTk.PhotoImage(Image.open("lacoste.png")),ImageTk.PhotoImage(Image.open("mcd.png")),ImageTk.PhotoImage(Image.open("spotify.png")),ImageTk.PhotoImage(Image.open("twitter.png")),ImageTk.PhotoImage(Image.open("netflix.png")),ImageTk.PhotoImage(Image.open("pringles.png")),ImageTk.PhotoImage(Image.open("starbucks.png")),ImageTk.PhotoImage(Image.open("kitkat.png")),ImageTk.PhotoImage(Image.open("nike.png"))]
    names=["Lacoste","MCDonalds","Spotify","Twitter","Netflix","Pringles","Starbucks","KitKat","Nike"]

    t.configure(bg="black")
    t.geometry("800x500")
    t.title("Guess the Logo Game!")
    titleLabel=Label(t,text=" GUESS  THE  LOGO  GAME ",font="Stencil 40 underline bold italic",fg="black").place(x=400,y=100)
    
    #placing image on window
    img=Label(t,image=pics[0])
    img.place(x=500,y=200)
    img.config(image=pics[0])
    number=0
    score=0

    #displaying Score
    ls=Label(t,text="Score ->",font="Stencil 20",fg="black")
    ls.place(x=1200,y=50)
    lss=Label(t,text=score,font="Stencil 20",fg="black")
    lss.place(x=1300,y=50)

    #prompting the user to enter choice
    l1=Label(t,text="Enter the name for this logo ",font="Stencil 25 bold",fg="black")
    l1.place(x=400,y=570)

    #Temporary taking input for logo
    e1=Entry(t,bg="grey",font="Signboard 20")
    e1.place(x=550,y=650)

    #Submit Button
    submitButton=Button(t,text=" Submit ",bd=5,font ="Bodoni 20 bold italic",fg="blue",bg="white",command=checkLogo)
    submitButton.place(x=600,y=700)

    #Quit the Game
    Quit=Button(t,text=" Quit ",bd=5,font ="Bodoni 20 bold italic",bg="white",command=exit)
    Quit.place(x=120,y=50)

    ps1=Label(t,text="PS: Enter the names with perfect Capital",fg="white",bg="red",font="Bodoni 16 italic")
    ps1.place(x=30,y=500)
    ps2=Label(t,text="letters and spaces to score",fg="white",bg="red",font="Bodoni 16 italic")
    ps2.place(x=30,y=550)
    
    t.mainloop()



