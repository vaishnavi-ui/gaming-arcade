import pygame
import random
from tkinter import *
import sqlite3
connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

#Destructs the previous window
def destructMain(window,val):
        global Id
        Id=val
        window.destroy()
        SnakeGameMain()


#Displays the game over window
def gameOver():
        global score,Id
        t=Tk()
        t.title("Scoreboard")
        t.configure(bg="lightskyblue")
        l=Label(t,text="GAME OVER! YOUR SCORE IS :",font="Times 15 bold",bg="lightskyblue",fg="black")
        l.pack()
        l1=Label(t,text=score,font="Times 20 bold",fg="black",bg="lightskyblue")
        l1.pack()
        sql="SELECT SNAKE FROM SCORE WHERE ID=?"
        cursor.execute(sql,[(Id)])
        val=cursor.fetchone()
        if val==None:
                val2=0                
        else:
                val2=val[0]
        val3=val2+score
        sql2="UPDATE SCORE SET SNAKE=? WHERE ID=?"
        cursor.execute(sql2,[val3,(Id)])
        connection.commit()
        cursor.execute("SELECT MAX(SNAKE) FROM SCORE")
        val=cursor.fetchone()
        val1=val[0]
        str2="HIGH SCORE: "+str(val1)
        str3="YOUR PREVIOUS SCORE: "+str(val2)
        str4="YOUR CURRENT SCORE: "+str(val3)
        l3=Label(t,text=str2,font="Times 15",fg="Black",bg="lightskyblue")
        l4=Label(t,text=str3,font="Times 15",fg="Black",bg="lightskyblue")
        l5=Label(t,text=str4,font="Times 15",fg="Black",bg="lightskyblue")
        l3.pack()
        l4.pack()
        l5.pack()
        
        b1=Button(t,text="Exit",width=10,height=2,font="Times 10 bold",bg="white",fg="black",command=t.destroy )
        b1.pack()
        b2=Button(t,text="Play Again",width=10,height=2,font="Times 10 bold",bg="white",fg="black",command=lambda: destructMain(t,Id))
        b2.pack()
        t.mainloop()

#Increases the snake length whenever it eats food
def increaseSnake(a,b,snake):
    global score
    snake.append([a,b])

#Displays the snake on the screen
def display(snake):
    global screen
    count=0
    for box in snake:
        if count%2==0:
            pygame.draw.rect(screen,(0,0,0),[box[0],box[1],10,10])
        else:
            pygame.draw.rect(screen,(213,50,80),[box[0],box[1],10,10])
        count=count+1
#Main Window of the game
def SnakeGameMain():
        global screen,score
        pygame.init()#must for all pygame modules
        screen=pygame.display.set_mode((500,500))
        pygame.display.set_caption("Snake Game")
        flag=False
        x=50
        y=50
        x1=0
        y1=0
        snake=[]
        snake.append([x,y])
        counter=0
        fx=250
        fy=250
        speed=5
        score=0
        #clock=pygame.time.Clock()
        while not flag:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    flag=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x1=-10
                        y1=0
                        
                    elif event.key==pygame.K_RIGHT:
                        x1=10
                        y1=0
                        
                    elif event.key==pygame.K_UP:
                        x1=0
                        y1=-10
                        
                    elif event.key==pygame.K_DOWN:
                        x1=0
                        y1=10                       
            x+=x1
            y+=y1
            x2=x
            y2=y    
            length=len(snake)            
            if x>500 or x<0 or y>500 or y<0:
                   flag=True
            screen.fill((50,153,213))
            increaseSnake(x,y,snake)
            if snake[-1][0]==fx and snake[-1][1]==fy:
                fx=round(random.randrange(0, 490)/10.0)*10.0
                fy=round(random.randrange(0, 490)/10.0)*10.0
                speed=speed+1
                score=score+10
            else:        
                del snake[0]
                
            for row in snake[:-1]:
                if row[0]==x and row[1]==y:
                    flag=True    
            pygame.draw.rect(screen,(0,255,0),[fx,fy,10,10])#makes food
            display(snake)
            pygame.display.update()
            pygame.time.Clock.tick(speed)
        pygame.quit()
        gameOver()
        
