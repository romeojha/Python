from turtle import Turtle
import time
from turtle import Turtle
class Cars(Turtle):
    def __init__(self,gotoo) -> None:
        super().__init__()
        self.shape('square')
        self.shapesize(1,3)
        self.penup()
        self.goto(gotoo)

    def singlerow(self):
        pass
# car2=Cars((400,100))
# car3=Cars((300,100))
# car4=Cars((200,100))
# car5=Cars((100,100))
# car6=Cars((0,0))
# car7=Cars((-100,100))
# car8=Cars((-200,100))


# # randomcar=random.choice('car1','car2','car3','car4','car5','car6','car7','car8')
# carlist=[car1,car2,car3,car4,car5,car6,car7,car8]

# def carloop():
#     for allcars in carlist:
#         return allcars

# allcars=carloop()

