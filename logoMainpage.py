from tkinter import *
from logo_game import *
from PIL import Image,ImageTk,ImageOps

def destructlogo(window,val):
    global ID
    ID=val
    window.destroy
    logoMain()
    
def logoMain():
    global ID
    
    lm=Toplevel()
    lm.title("Logo game cover")
    lm.configure(bg="black")
    ctitle=Label(lm,text="Welcome to the logo game",font="Times 30 bold italic underline",fg="white",bg="black")
    ctitle.grid(row=0,column=3)

    i1=ImageTk.PhotoImage(Image.open("mcd.png"))
    l1=Label(lm,image=i1)
    l1.grid(row=0,column=0)

    i2=ImageTk.PhotoImage(Image.open("twitter.png"))
    l2=Label(lm,image=i2)
    l2.grid(row=0,column=1)

    i3=ImageTk.PhotoImage(Image.open("nike.png"))
    l3=Label(lm,image=i3)
    l3.grid(row=0,column=2)

    i4=ImageTk.PhotoImage(Image.open("starbucks.png"))
    l4=Label(lm,image=i4)
    l4.grid(row=1,column=0)

    i5=ImageTk.PhotoImage(Image.open("netflix.png"))
    l5=Label(lm,image=i5)
    l5.grid(row=1,column=1)

    i6=ImageTk.PhotoImage(Image.open("lacoste.png"))
    l6=Label(lm,image=i6)
    l6.grid(row=1,column=2)

    i7=ImageTk.PhotoImage(Image.open("kitkat.png"))
    l7=Label(lm,image=i7)
    l7.grid(row=2,column=0)

    i8=ImageTk.PhotoImage(Image.open("spotify.png"))
    l8=Label(lm,image=i8)
    l8.grid(row=2,column=1)

    i9=ImageTk.PhotoImage(Image.open("pringles.png"))
    l9=Label(lm,image=i9)
    l9.grid(row=2,column=2)

    cb=Button(lm,text=" Wanna play? ",font="Verdana 25 italic",bg="white",fg="#002593",command=lambda: destructLogoGame(lm,ID))
    cb.grid(row=1,column=3)

    q=Button(lm,text=" Quit ",font="Verdana 25 italic",bg="white",fg="#002593",command=lm.destroy)
    q.grid(row=2,column=3)

    lm.mainloop()
