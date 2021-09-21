from turtle import Turtle
START_POS=[(-40,0),(-20,0),(0,0)]
MOVING_DISTANCE=20

class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in START_POS:
            part1=Turtle(shape='square')
            part1.color('red')
            part1.penup()
            part1.goto(pos)
            self.snake_body.append(part1)

    def move(self):
        for part in range(len(self.snake_body)-1,0,-1):
            x_cor=self.snake_body[part-1].xcor()
            y_cor=self.snake_body[part-1].ycor()
            self.snake_body[part].goto(x_cor,y_cor)
        self.snake_body[0].forward(MOVING_DISTANCE)
    
    def Up(self):
        self.snake_body[0].setheading(90)
    def Down(self):
        self.snake_body[0].setheading(270)
    def Right(self):
        self.snake_body[0].setheading(360)
    def Left(self):
        self.snake_body[0].setheading(180)