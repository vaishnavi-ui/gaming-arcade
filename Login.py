from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from Register import *
from Scoreboard import *
import sqlite3

connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()
def destroyLogin(window):
    window.destroy()
    LoginGUI()
def check():
    global log
    global e1,e2
    if len(e1.get())>0 and len(e2.get())>0:        
        find1=("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?")
        cursor.execute(find1,[(e1.get()),(e2.get())])
        val=cursor.fetchone()
        if val is not None:
            ID=val[0]
            msg=Label(log,text="LOGIN SUCCESSFUL!",font="Verdana 20",bg="black",foreground="snow").place(x=400,y=500)
            b2=Button(log,text="View Scoreboard?",font="Verdana 20",command=lambda: destructScore(log,ID)).place(x=700,y=500)
            
        else:
            msg=Label(log,text="UNSUCCESSFUL LOGIN",font="Verdana 20",bg="black",foreground="snow").place(x=400,y=500)
            b3=Button(log,text="Register first?",font="Verdana 20",command=lambda: destroyRegister(log)).place(x=450,y=550)
            b4=Button(log,text="Login again?",font="Verdana 20",command=lambda: destroyLogin(log)).place(x=700,y=550)
    else:
        messagebox.showerror("Error","Please fill all fields!")
    
    
def LoginGUI():
    global log,e1,e2    
    log=Toplevel()
    log.title("Login Page")
    img=ImageTk.PhotoImage(Image.open("bg1.png"))
    lg=Label(log,image=img).place(x=0,y=0)
    l=Label(log,text="Log into your existing account",font="Verdana 30 bold italic").place(x=400,y=50)
    l1=Label(log,text="USERNAME:",font="Verdana 20",bg="black",foreground="snow").place(x=500,y=150) 
    l2=Label(log,text="PASSWORD:",font="Verdana 20",bg="black",foreground="snow").place(x=500,y=250)

    e1=Entry(log,font="Verdana 20")
    e1.place(x=700,y=150)
    e2=Entry(log,font="Verdana 20")
    e2.place(x=700,y=250)

    b1=Button(log,text="Submit",command=check,font="Verdana 20").place(x=650,y=350)
    log.mainloop()

