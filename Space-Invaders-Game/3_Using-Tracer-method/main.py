from turtle import Screen
from player import Player
import time 

screen = Screen()
screen.setup(600, 600)
screen.setup(600, 600)
screen.tracer(0)


player = Player()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    screen.exitonclick()


screen.exitonclick()