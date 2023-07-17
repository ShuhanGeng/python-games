import time 
from turtle import Screen
from player import Player
from invader import Invader

# create a new game window
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# create a new player object
player = Player()
invader = Invader()

try:  
    # listen for arrow key events and exit on ESC key
    screen.listen()
    screen.onkey(player.turn_left, "Left")
    screen.onkey(player.turn_right, "Right")
    screen.onkey(player.create_missile, "space")
    screen.onkey(screen.bye, "Escape")

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        player.fire()
        invader.create_invader()
        invader.move()
        screen.update()
        if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
            game_is_on = False
            
        for m in player.missiles:
            for i in invader.enemies:
                if m.distance(i) < 20:
                    player.missiles.remove(m)
                    invader.enemies.remove(i)
                    m.hideturtle()
                    i.hideturtle()

            if m.distance(player)>600:
                player.missiles.remove(m)
                m.hideturtle()
    
    screen.bye()
except Exception as er:
    pass