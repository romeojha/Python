from turtle import Screen, xcor, ycor
from ping import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height=800, width=800)
screen.tracer(0)

lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(rpaddle.goup, 'Up')
screen.onkey(rpaddle.godown, 'Down')

#here i created different goup and gown to use for "w" and "s". not needed

screen.onkey(lpaddle.goup, 'w')
screen.onkey(lpaddle.godown, 's')

y_score = 0
x_score = 0
game = True
while game:

    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 341 or ball.ycor() < -341:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(rpaddle) < 50 or ball.xcor(
    ) < -320 and ball.distance(lpaddle) < 50:
        ball.bounce_x()
    elif ball.xcor() > 360:
        ball.reset()
        y_score += 1
        print("Score of A :", y_score)
    elif ball.xcor() < -360:
        ball.reset
        x_score += 1
        print("Score of B :", x_score)

screen.exitonclick()
