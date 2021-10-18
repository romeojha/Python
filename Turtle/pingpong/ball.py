from turtle import Turtle
import time


#we can also import through the main like this
"""
    ball=turtle()
    ball.penup()
    ball.shape('square')
    ball.pos(x,y)
"""


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setpos(0,0)
        self.xmov=10
        self.ymov=10


    def move(self):
        x_move=self.xcor()+self.xmov
        y_move=self.ycor()+self.ymov
        self.goto(x_move,y_move)


    def bounce_y(self):
       self.ymov *= -1
    
    def bounce_x(self):
        self.xmov *= -1

    def reset(self):
        time.sleep(1)
        self.goto(0,0)

