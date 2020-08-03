from tkinter import *
from tkinter import messagebox
import sqlite3
connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()
import time
count=0

#Destructs the previous window
def destructXO(window,val):
    global ID
    ID=val
    window.destroy()
    TicTacToeGUI()

#Whenever the user selects the quit option, this message is displayed
def Quit():
    global t    
    msg=messagebox.askquestion("Confirm","Are you want to Quit? You still have chances!")
    if msg=='yes':
        t.destroy()

#Destructs the winner window and game window
def destruct():
    global t,winnerWindow
    t.destroy()
    winnerWindow.destroy()

#Displays the winning condition
def displayWinner(winner):
    global t,winnerWindow,ID    
    winnerWindow=Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l1=Label(winnerWindow,text="THE WINNER IS: ",font="Times 15",bg="Black",fg="White")
    l1.pack()
    str1="PLAYER "+str(winner)
    l2=Label(winnerWindow,text=str1,font="Times 15",bg="Black",fg="White")
    l2.pack()
    sql="SELECT TICTACTOE FROM SCORE WHERE ID=?"
    cursor.execute(sql,[(ID)])
    val=cursor.fetchone()
    if val==None:
        val2=0                
    else:
        val2=val[0]
    
    if winner=="1":
        sql2="UPDATE SCORE SET TICTACTOE=TICTACTOE+10 WHERE ID=?"
        cursor.execute(sql2,[(ID)])
        connection.commit()
        val3=val2+10
    else:
        val3=val2
    cursor.execute("SELECT MAX(TICTACTOE) FROM SCORE")
    val=cursor.fetchone()
    val1=val[0]
    str2="HIGH SCORE: "+str(val1)
    str3="YOUR PREVIOUS SCORE: "+str(val2)
    str4="YOUR CURRENT SCORE: "+str(val3)
    l3=Label(winnerWindow,text=str2,font="Times 15",bg="Black",fg="White")
    l4=Label(winnerWindow,text=str3,font="Times 15",bg="Black",fg="White")
    l5=Label(winnerWindow,text=str4,font="Times 15",bg="Black",fg="White")
    l3.pack()
    l4.pack()
    l5.pack()
    bproceed=Button(winnerWindow,text="Proceed",font=("COMIC SANS MS",10,"bold italic"),command=destruct)
    bproceed.pack()

#Checks for the winner        
def checkWinner():
    global count,b1,b2,b3,b4,b5,b6,b7,b8,b9
    if (b1["text"]==b2["text"]==b3["text"]=="X" or b4["text"]==b5["text"]==b6["text"]=="X" or b7["text"]==b8["text"]==b9["text"]=="X" or
        b1["text"]==b4["text"]==b7["text"]=="X" or b2["text"]==b5["text"]==b8["text"]=="X" or b3["text"]==b6["text"]==b9["text"]=="X" or
        b1["text"]==b5["text"]==b9["text"]=="X" or b3["text"]==b5["text"]==b7["text"]=="X"):
        displayWinner("1")
    elif (b1["text"]==b2["text"]==b3["text"]=="O" or b4["text"]==b5["text"]==b6["text"]=="O" or b7["text"]==b8["text"]==b9["text"]=="O" or
          b1["text"]==b4["text"]==b7["text"]=="O" or b2["text"]==b5["text"]==b8["text"]=="O" or b3["text"]==b6["text"]==b9["text"]=="O" or
          b1["text"]==b5["text"]==b8["text"]=="O" or b3["text"]==b5["text"]==b7["text"]=="O"):
        displayWinner("2")
    elif count==9:
        displayWinner("NONE! IT IS A TIE!")

#Changes the value of the button
def changeVal(button):
    global count
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(t,text="PLAYER: 2(O)",height=3,font=("COMIC SANS MS",10,"bold italic"),bg="white").grid(row=0,column=0)
        else:
            button["text"]="O"
            l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold italic"),bg="white").grid(row=0,column=0)
        count=count+1
        checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")

#Displays the GUI 
def TicTacToeGUI():
    global t,b1,b2,b3,b4,b5,b6,b7,b8,b9
    t=Tk()
    t.title("TIC TAC TOE")
    t.configure(bg="white")
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold italic"),bg="white").grid(row=0,column=0)
    b1=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b1))
    b2=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b2))
    b3=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b3))
    b4=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b4))
    b5=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b5))
    b6=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b6))
    b7=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b7))
    b8=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b8))
    b9=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b9))

    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)

    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)

    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)

    exitButton=Button(t,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold italic")).grid(row=0,column=2)

