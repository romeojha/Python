from turtle import Turtle



class Paddle(Turtle):             #paddle=Turtle()
                                    #using inheritance
    def __init__(self,poss):
        super() .__init__()
        self.penup()      #used to be paddle.penup
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(poss)


    def goup(self):
        new_y = self.ycor() + 40                #used to be paddle.ycor()
        self.goto(self.xcor(), new_y)

    def godown(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
    



#i created it but it was of no need as func goup and godown do the job
    # def gow(self):
    #     new_y = self.ycor() + 40
    #     self.goto(self.xcor(), new_y)

    # def gos(self):
    #     new_y = self.ycor() - 40
    #     self.goto(self.xcor(), new_y)


    



    