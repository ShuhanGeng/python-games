import time 
from turtle import Screen
from player import Player

# create a new game window
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# create a new player object
player = Player()


try:  
    # listen for arrow key events and exit on ESC key
    screen.listen()
    screen.onkey(player.turn_left, "Left")
    screen.onkey(player.turn_right, "Right")
    screen.onkey(screen.bye, "Escape")

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
            game_is_on = False
    
    screen.bye()
except Exception as er:
    pass