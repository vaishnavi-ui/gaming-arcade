from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
from SnakeGameMainPage import *
from TicTacToeMainPage import *
from logoMainpage import *
from hangman import *
from colour_game import *
def destructHomepage(window,value):
    global ID
    ID=value
    window.destroy()
    HomepageGUI()
def HomepageGUI():
    global home,ID
    home=Toplevel()
    home.title("home page")
    home.geometry("800x500")
    home.configure(bg="black")
    l=Label(home,text="WELCOME TO THE HOME PAGE",font="Verdana 30 bold italic",foreground="royal blue").place(x=420,y=60)
    l1=Label(home,text="Choose a game and have fun at the gaming arcade!",font="Verdana 25 bold",foreground="black").place(x=300,y=120)

    p1=ImageTk.PhotoImage(Image.open("logobutton.png"))
    #pp1=p1.subsample(2,2)
    b1=Button(home,text="LOGO GAME",image=p1,compound=TOP,command=lambda:destructlogo(home,ID)).place(x=130,y=350)

    p2=ImageTk.PhotoImage(Image.open("tictacbutton.png"))
    #pp2=p2.subsample(2,2)
    b2=Button(home,text="TIC TAC TOE",image=p2,compound=TOP,command=lambda:XOMainPage(ID)).place(x=500,y=200)

    p3=ImageTk.PhotoImage(Image.open("hangmanbutton.png"))
    #pp3=p3.subsample(2,2)
    b3=Button(home,text="HANGMAN ",image=p3,compound=TOP,command=lambda:destructHangmanGame(home,ID)).place(x=800,y=200)
    
    p4=ImageTk.PhotoImage(Image.open("snakebutton.png"))
    #pp4=p4.subsample(2,2)
    b4=Button(home,text="SNAKE GAME",image=p4,compound=TOP,command=lambda:SnakeGameGUI(ID)).place(x=500,y=500)

    p5=ImageTk.PhotoImage(Image.open("colourbutton.png"))
    #pp5=p5.subsample(2,2)
    b5=Button(home,text="COLOUR GAME",image=p5,compound=TOP,command=lambda:destructColourGame(home,ID)).place(x=800,y=500)
    
    home.mainloop()



