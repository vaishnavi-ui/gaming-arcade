from tkinter import *
from PIL import Image,ImageTk
from Register import *
from Login import *

t=Tk()
t.title("Welcome page")

img=ImageTk.PhotoImage(Image.open("bg1.png"))
lg=Label(t,image=img).place(x=0,y=0)
l1=Label(t,text="WELCOME TO THE GAMING ARCADE!",font="Verdana 35 bold italic",bg="black",fg="white").place(x=250,y=100)
lgame=Label(t,text="We have the following games: ",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=160)
lsnake=Label(t,text="SNAKE GAME",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=220)
lhangman=Label(t,text="HANGMAN",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=280)
ltic=Label(t,text="TIC TAC TOE",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=340)
lguess=Label(t,text="GUESS THE LOGO",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=400)
lbrain=Label(t,text="COLOR GAME",font="Verdana 15  italic",height=2,width=74,bg="black",fg="white").place(x=250,y=460)

l2=Label(t,text="NEW USER? JUST REGISTER AND PLAY!",font="Verdana 13 italic",bg="black",fg="white").place(x=870,y=560)

b1=Button(t,text="Login !",font="Verdana 20 underline",activebackground="blue",bg="black",fg="white",command=lambda: destroyLogin(t)).place(x=300,y=600)

l3=Label(t,text="ALREADY HAVE AN ACCOUNT? LOGIN TO PROCEED!",font="Verdana 13 italic",bg="black",fg="white").place(x=250,y=560)

b2=Button(t,text="Register ?",font="Verdana 20 underline",activebackground="blue",bg="black",fg="white",command=lambda: destroyRegister(t)).place(x=950,y=600)

t.mainloop()
