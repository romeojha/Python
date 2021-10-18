from turtle import Screen , distance
import time
from snake import Snake
from food import Food

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title(' snake Game')
screen.tracer(0)

snake=Snake()

food=Food()

screen.listen()
screen.onkey(snake.Up,'Up')
screen.onkey(snake.Left  ,'Left')
screen.onkey(snake.Down,'Down')
screen.onkey(snake.Right,'Right')



game_on=True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()


if snake.head.distance(food)<15:
    print('nom')
    
        
        
        



        
        




screen.exitonclick()