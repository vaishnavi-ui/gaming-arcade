from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import string
import sqlite3
connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

life=0
score=0
str1=""

char_list=list()
entered=list()

def destructHangmanGame(window,val):
        global ID
        ID=val
        HangmanGUI()
def exits():
    global score
    global ID
    global hg
    t=Tk()
    t.title("Scoreboard")
    l=Label(t,text="GAME OVER! YOUR SCORE IS :",font="Signboard 22 bold underline")
    l.pack()
    l1=Label(t,text=score,font="Signboard 22 bold")
    l1.pack()
    sql="SELECT HANGMAN FROM SCORE WHERE ID=?"
    cursor.execute(sql,[(ID)])
    val=cursor.fetchone()
    if val==None:
            val2=0
    else:
            val2=val[0]
    val3=val2+score
    sql2="UPDATE SCORE SET HANGMAN=? WHERE ID=?"
    cursor.execute(sql2,[val3,(ID)])
    connection.commit()

    cursor.execute("SELECT MAX(HANGMAN) FROM SCORE")
    val=cursor.fetchone()
    val1=val[0]
    str2="HIGH SCORE: "+str(val1)
    str3="YOUR PREVIOUS SCORE: "+str(val2)
    str4="YOUR CURRENT SCORE: "+str(val3)
    l3=Label(t,text=str2,font="Signboard 22 bold")
    l4=Label(t,text=str3,font="Signboard 22 bold")
    l5=Label(t,text=str4,font="Signboard 22 bold")
    l3.pack()
    l4.pack()
    l5.pack()
    hg.destroy()
        
    b1=Button(t,text="QUIT?",font="Signboard 20 bold",bg="white",fg="black",command=t.destroy)
    b1.pack()
    t.mainloop()
    
def new_game():
    global life
    global all_words
    global char_list
    global entered
    global pics
    global hg
    
    life=11
    entered=[]
    word=random.choice(all_words)
    char_list=list(word)
    length=len(word)
    for i in range(0,length):
        entered.append("_")
    img=Label(hg,image=pics[0])
    img.place(x=120,y=200)
    img.config(image=pics[0])

    l6=Label(hg,text="                          ",fg="#BD081C",bg="#BD081C",font="Signboard 20")
    l6.place(x=790,y=450)
    l6=Label(hg,text=entered,bg="#BD081C",foreground="#feda84",font="Signboard 20")
    l6.place(x=790,y=450)
 
    l4=Label(hg,text="                                                                          ",fg="#BD081C",bg="#BD081C",font="Signboard 17 bold")
    l4.place(x=180,y=50)
    l4=Label(hg,text=life,foreground="#95daf8",bg="#BD081C",font="Signboard 17 bold")
    l4.place(x=180,y=50)
    
        
def guess():
    global e1
    global hg
    global pics
    global entered
    global life
    global char_list
    global score


    if life>=0:
        if char_list.count(e1.get())>0:
            
            for i in range(0,len(char_list)):
                if(e1.get()==char_list[i]):
                    entered[i]=str(e1.get())
                elif(entered[i]=="_"):
                    entered[i]="_"
                l6=Label(hg,text="                      ",fg="#BD081C",bg="#BD081C",font="Signboard 20")
                l6.place(x=790,y=450)
                l6=Label(hg,text=entered,bg="#BD081C",foreground="#feda84",font="Signboard 20")
                l6.place(x=790,y=450)

                l4=Label(hg,text="                                                              ",fg="#BD081C",bg="#BD081C",font="Signboard 17 bold")
                l4.place(x=170,y=50)
                l4=Label(hg,text=life,foreground="#95daf8",bg="#BD081C",font="Signboard 17 bold")
                l4.place(x=170,y=50)
                if(entered==char_list):
                    messagebox.showinfo("game","CORRECT ANSWER")
                    score=score+1

                    lss=Label(hg,text="                ",fg="#BD081C",bg="#BD081C",font="Signboard 15 bold underline")
                    lss.place(x=1300,y=50)
                    lss=Label(hg,text=score,foreground="#95daf8",bg="#BD081C",font="Signboard 15 bold underline")
                    lss.place(x=1300,y=50)
                    new_game()
        else:
            life-=1
            img=Label(hg,image=pics[11-life])
            img.place(x=120,y=200)

             
            l6=Label(hg,text="                        ",fg="#BD081C",bg="#BD081C",font="Signboard 20")
            l6.place(x=790,y=450)
            l6=Label(hg,text=entered,bg="#BD081C",foreground="#feda84",font="Signboard 20")
            l6.place(x=790,y=450)

            l4=Label(hg,text="                                                              ",fg="#BD081C",bg="#BD081C",font="Signboard 17 bold")
            l4.place(x=180,y=50)
            l4=Label(hg,text=life,foreground="#95daf8",bg="#BD081C",font="Signboard 17 bold")
            l4.place(x=180,y=50)
     
            if life==0:
                messagebox.showwarning("game","WRONG ANSWER")
                exits()

def HangmanGUI():
    global hg
    global e1
    global pics
    global all_words
    global score
    
    hg=Toplevel()
    score=0
    pics=[ImageTk.PhotoImage(Image.open("hang0.png")),ImageTk.PhotoImage(Image.open("hang1.png")),ImageTk.PhotoImage(Image.open("hang2.png")),ImageTk.PhotoImage(Image.open("hang3.png")),ImageTk.PhotoImage(Image.open("hang4.png")),ImageTk.PhotoImage(Image.open("hang5.png")),ImageTk.PhotoImage(Image.open("hang6.png")),ImageTk.PhotoImage(Image.open("hang7.png")),ImageTk.PhotoImage(Image.open("hang8.png")),ImageTk.PhotoImage(Image.open("hang9.png")),ImageTk.PhotoImage(Image.open("hang10.png")),ImageTk.PhotoImage(Image.open("hang0.png"))]
    #the list containing all words for hangman game
    all_words=["tkinter","classes","objects","library","strings","bitwise","comment","looping","default","mutable","slicing","keyword","buttons"]

    hg.title("Hangman game")
    hg.configure(bg="#BD081C")
    new_game()

    img=Label(hg,image=pics[0])
    img.place(x=120,y=200)
    img.config(image=pics[0])

    l1=Label(hg,text="Welcome to the Hangman Game",font="Verdana 30",foreground="#feda84",bg="#BD081C")
    l1.place(x=400,y=80)

    l2=Label(hg,text="Enter your guess letter ",font="Signboard 20",foreground="#95daf8",bg="#BD081C")
    l2.place(x=570,y=250)

    e1=Entry(hg,bg="#feda84",font="Signboard 20")
    e1.place(x=610,y=300)
    
    b1=Button(hg,text=" Submit ",command=guess,fg="blue",font="Signboard 20")
    b1.place(x=680,y=380)

    #displaying the lives left in game
    l3=Label(hg,text="Life->",foreground="#95daf8",bg="#BD081C",font="Signboard 15 bold underline")
    l3.place(x=100,y=50)

    l4=Label(hg,text=life,foreground="#95daf8",bg="#BD081C",font="Signboard 15 bold")
    l4.place(x=180,y=50)

    #displaying the score of the player
    ls=Label(hg,text="Score->",foreground="#95daf8",bg="#BD081C",font="Signboard 15 bold underline")
    ls.place(x=1220,y=50)

    lss=Label(hg,text="                         ",fg="#BD081C",bg="#BD081C",font="Signboard 15 bold underline")
    lss.place(x=1300,y=50)
    lss=Label(hg,text=score,foreground="#95daf8",bg="#BD081C",font="Signboard 15 bold underline")
    lss.place(x=1300,y=50)

    new_game()
    l5=Label(hg,text="Current Status:",font="Helvetica 24",foreground="#95daf8",bg="#BD081C")
    l5.place(x=550,y=450)

    l6=Label(hg,text=entered,bg="#BD081C",foreground="#feda84",font="Signboard 20")
    l6.place(x=790,y=450)

    im=ImageTk.PhotoImage(Image.open("rules.png"))
    rule=Label(hg,image=im).place(x=500,y=500)

    lmsg=Label(hg,text="PS: These words belong to python language",font="Signboard 15 italic",foreground="#95daf8",bg="#BD081C")
    lmsg.place(x=20,y=600)

    q=Button(hg,text="Exit",font="Signboard 20",fg="blue",command=exits).place(x=180,y=650)

    hg.mainloop()





