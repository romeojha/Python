
import turtle as t
from turtle import Screen as Sc
import random

a_turtle = t.Turtle()
a_turtle.pensize(15)
a_turtle.speed(5)
t.colormode(255)


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def circular_draw():
    for i in range(90):
        a_turtle.position()
        a_turtle.color(randomcolor())
        a_turtle.circle(350)
        a_turtle.left(4)
        a_turtle.fd(10)


def art():
    for val in range(10):
        a_turtle.penup()
        a_turtle.setposition(-500, -300+(val*100))
        a_turtle.pendown
        for i in range(10):
            a_turtle.color(randomcolor())
            a_turtle.dot(50)
            a_turtle.penup()
            a_turtle.fd(100)
            a_turtle.pendown()
            a_turtle.hideturtle()


def pentagon(value, val):
    for i in range(5):
        a_turtle.left(value)
        a_turtle.fd(val)


def randomWalk():
    angle = [0, 90, 270]
    for i in range(500):
        a_turtle.left(random.choice(angle))
        a_turtle.color(randomcolor())
        a_turtle.fd(30)
        # a_turtle.penup()
        # a_turtle.fd(30)
        # a_turtle.pendown()


# art()
randomWalk()
screen = Sc()
screen.exitonclick()
