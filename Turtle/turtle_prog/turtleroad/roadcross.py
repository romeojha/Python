import time
from turtle import Turtle,Screen
from cars import Cars
from random import random

screen=Screen()
turtle=Turtle()
screen.tracer(0)
screen.screensize(600,600)
turtle.shape('turtle')
turtle.penup()
turtle.goto(0,-300)
turtle.setheading(90)

def moveup():
    turtle.forward(20)

screen.listen()
screen.onkey(moveup,"Up")



car1=Cars((500,-200))
car2=Cars((300,-200))
car3=Cars((100,-20))



game_is_on=True

def createcars():
    return Cars((500,100))


while game_is_on:

    screen.update()
    new_car=createcars()
    car1.back(20) 
    car2.back(20) 
    car3.back(20) 
    new_car.back(20)
    time.sleep(.2)



screen.exitonclick()