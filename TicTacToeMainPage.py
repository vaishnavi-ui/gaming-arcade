from tkinter import *
from TicTacToe import *
from PIL import Image,ImageOps
def XOMainPage(ID):

    t=Tk()
    t.title("Snake Game")
    t.geometry("450x460")
    l=Label(t,text="TIC",height=4,width=8,bg="black",fg="white",font=("Fantasy",15,"bold italic")).grid(row=0,column=0)
    l1=Label(t,text="TAC",height=6,width=12,bg="white",fg="black",font=("Fantasy",15,"bold italic")).grid(row=0,column=1)
    l2=Label(t,text="TOE",height=4,width=8,bg="black",fg="white",font=("Fantasy",15,"bold italic")).grid(row =0,column=2)
    b1=Label(t,text="Get yourself",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=3,column=0)
    b7=Label(t,text="a partner",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=4,column=0)
    b8=Label(t,text=" to play!",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=5,column=0)
    b2=Label(t,text="",height=2,width=12,bg="black",activebackground="white",fg="white",font="Times 15 bold").grid(row=3,column=1)
    b11=Label(t,text="",height=2,width=12,bg="black",activebackground="white",fg="white",font="Times 15 bold").grid(row=4,column=1)
    b12=Label(t,text="",height=2,width=12,bg="black",activebackground="white",fg="white",font="Times 15 bold").grid(row=5,column=1)
    b13=Label(t,text="If you win",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=3,column=2)
    b9=Label(t,text="you get",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=4,column=2)
    b10=Label(t,text="10 points!",height=2,width=12,bg="white",fg="black",font="Times 15 bold").grid(row=5,column=2)
    b4=Button(t,text="QUIT",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=t.destroy)
    b5=Label(t,text="",height=6,width=12,bg="white",fg="black",font="Times 15 bold")
    b6=Button(t,text="PLAY",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: destructXO(t,ID)) 
    b4.grid(row=6,column=0)
    b5.grid(row=6,column=1)
    b6.grid(row=6,column=2)

    

