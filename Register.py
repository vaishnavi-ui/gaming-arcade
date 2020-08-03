from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from Homepage import *
import sqlite3

connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

def destroyRegister(window):
    window.destroy()
    RegisterGUI()
    
def validatePassword(password):
    global r,e1,e2,e3
    if len(e1.get())>0 and len(e2.get())>0 and len(e3.get())>0:
        for ch in e1.get():
            if ch.isdigit():
                messagebox.showerror("Error","Name cannot have digits!")
                break
        sql1="SELECT COUNT(ID) FROM USERS WHERE USERNAME=?"
        cursor.execute(sql1,[(e2.get())])
        val=cursor.fetchone()
        val1=val[0]
        if val1==0: 
            store=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&]).{5,}$")     
            if  re.search(store, password): 
                l1=Label(r,text="Password is valid.",font="Verdana 26",bg="black",fg="white")
                l1.place(x=400,y=600)
                b2=Button(r,text="Register",command=enter,font="Verdana 20")
                b2.place(x=500,y=650)
                
            else:
                messagebox.showerror("Error","Password is invalid! Please try another!")

        else:
            messagebox.showerror("Error","This Username already exists! Please try another!")
            
    else:
        messagebox.showerror("Error","Please fill all fields!")
    
def enter():
    global r
    global e1,e2,e3
    find1=("INSERT INTO USERS(NAME,USERNAME,PASSWORD) VALUES(?,?,?)")
    cursor.execute(find1,[(e1.get()),(e2.get()),(e3.get())])
    connection.commit()
    lsuccess=Label(r,text="You have been sucessfully registered! Click to play Games!",font="Verdana 15",bg="black",fg="white")
    lsuccess.place(x=450,y=700)
    cursor.execute("SELECT MAX(ID) FROM USERS")
    val=cursor.fetchone()
    ID=val[0]
    sql1=("INSERT INTO SCORE(ID) VALUES (?)")
    cursor.execute(sql1,[(ID)])
    connection.commit()
    bplay=Button(r,text="Play",font="Verdana 10",command=lambda: destructHomepage(r,ID))
    bplay.place(x=600,y=750)

def RegisterGUI():
    global r,e1,e2,e3
    #t=Tk()
    r=Toplevel()
    r.title("Register Page")
    img=ImageTk.PhotoImage(Image.open("bg1.png"))
    lg=Label(r,image=img).place(x=0,y=0)

    l=Label(r,text="Welcome to Register!",font="Verdana 25 bold italic",bg="black",fg="white").place(x=500,y=50)
 
    l1=Label(r,text="Please enter the following details",font="Verdana 20",bg="black",fg="white").place(x=500,y=150)

    
    l2=Label(r,text="NAME",font="Verdana 18",bg="black",fg="white").place(x=100,y=250)

    
    l3=Label(r,text="USERNAME",font="Verdana 18",bg="black",fg="white").place(x=100,y=300)

    
    l4=Label(r,text="PASSWORD",font="Verdana 18",bg="black",fg="white").place(x=100,y=350)

    
    l5=Label(r,text="Please enter a password with following parameters: ",font="Verdana 15",bg="black",fg="white").place(x=600,y=250)

    
    l6=Label(r,text="1. Should have at least one number.",font="Verdana 15",bg="black",fg="white").place(x=600,y=300)

    
    l7=Label(r,text="2. Should have at least one uppercase and one lowercase character.",font="Verdana 15",bg="black",fg="white").place(x=600,y=350)

    
    l8=Label(r,text="3. Should have at least one special symbol.",font="Verdana 15",bg="black",fg="white").place(x=600,y=400)

    
    l9=Label(r,text="4. Should have more than 6 characters.",font="Verdana 15",bg="black",fg="white").place(x=600,y=450)
   
    
    e1=Entry(r)
    e1.place(x=300,y=250)
   
    
    e2=Entry(r)
    e2.place(x=300,y=300)
  
    
    e3=Entry(r)
    e3.place(x=300,y=350)


    b1=Button(r,text=" Check Password ",width=15,height=2,font="Verdana 10",command=lambda: validatePassword(e3.get()))
    b1.place(x=100,y=400)

    r.mainloop()
   
