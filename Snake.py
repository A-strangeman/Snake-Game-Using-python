import turtle
import random
import time
import sys
from tkinter import messagebox

delay=0.1
#scoreboard Value
sc=0
#Highest Value
hs=0

#creating a body
bodies=[]
 #creating a Screen

s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600,height=600)   #size of the Screen


#creating a head
h=turtle.Turtle()
h.speed(0)
h.shape("square")
h.color("black")
h.fillcolor("black")
h.penup()
h.goto(0,0)
h.direction ="stop"

#creating Food for snake
i=turtle.Turtle()
i.speed(0)
i.shape("circle")
i.shapesize(0.5)
i.color("black")
i.fillcolor("red")
i.penup()
i.ht()
i.goto(150,200)
i.st()


#creating a Scoreboard
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-290,280)
sb.write("Score:0   | HighestScore:0")



def moveup():
    if h.direction != "down":
        h.direction ="up"
def movedown():
    if h.direction != "up":
        h.direction ="down"
def moveleft():
    if h.direction != "right":
        h.direction ="left"
def moveright():
    if h.direction != "left":
        h.direction ="right"
def movestop():
    h.direction = "Stop"


def move():
    if h.direction == 'up':
        y =h.ycor()
        h.sety(y+20)
    if h.direction =="down":
        y=h.ycor()
        h.sety(y-20)
    if h.direction =="left":
        x=h.xcor()
        h.setx(x-20)
    if h.direction =="right":
        x=h.xcor()
        h.setx(x+20)
#event Handling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")


#mainloop
while True:
    s.update()
    #collision with border
    if h.xcor()>290:
        h.setx(-290)
    if h.xcor()<-290:
        h.setx(290)
    if h.ycor()>290:
        h.sety(-290)
    if h.ycor()<-290:
        h.sety(290)
    #check Collision with food
    if h.distance(i)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        i.goto(x,y)
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)
        sc=sc+10
        delay=delay-0.001
        if sc>hs:
            hs=sc
        sb.clear()
        sb.write("Score:{}    | Highest Score:{}".format(sc,hs))
    #move Snake Bodies moving

    for j in range(len(bodies)-1,0,-1):
        x = bodies[j - 1].xcor()
        y = bodies[j - 1].ycor()
        bodies[j].goto(x, y)

    if len(bodies)>0:
        x=h.xcor()
        y=h.ycor()
        bodies[0].goto(x,y)
    move()
#check collision with snake
    for body in bodies:
        if body.distance(h)<20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"
            retry=messagebox.askretrycancel("Game Over", "Try again?")
            if not retry:
                sys.exit()

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay = 0.1
            sb.clear()
            sb.write("Score:{}   | Highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()    



