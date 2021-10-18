# from blackjack.blackjack import you_won
from turtle import Turtle, Screen, clear, color, fillcolor
import turtle
import random

screen = Screen()
screen.setup(height=800, width=1000)

turtle1 = Turtle()
turtle1.penup()
turtle1.setposition(300, 300)
turtle1.pendown()
turtle1.right(90)
turtle1.fd(600)

user_ans = screen.textinput(title="betting game",
                            prompt='bet on which coloured turtle will win the game/n')
color1 = ['red', 'blue', 'green', 'orange', 'purple', 'black']
turtle_list = []


for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.shapesize(3, 3)
    new_turtle.color(color1[i])
    new_turtle.penup()
    new_turtle.goto(x=-400, y=300-(i*100))
    turtle_list.append(new_turtle)

condition = True if user_ans else False

while condition:
    for new_turtle in turtle_list:
        new_turtle.forward(random.randint(1, 10))
        check_pos = new_turtle.position()
        if check_pos > (300, 1000):
            condition = False
            wincolor = new_turtle.color()
            if wincolor[1] == user_ans:
                print(f'you won {wincolor[1]}')
            else:
                print(f'you lose.winner is {wincolor[1]} ')


screen.exitonclick()
