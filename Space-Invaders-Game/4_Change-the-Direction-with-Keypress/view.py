import turtle
from player import Player
import time

# render the GUI window
ws = turtle.Screen()
ws.title("Python Course - Doing Space Invaders Game with Turtle Module")
bgcolor = 'wheat'
ws.bgcolor(bgcolor)
ws.setup(width=1200, height=800)
ws.tracer(0)

# instantiate a new turtle pen for rendering
tp = turtle.Turtle()
tp.penup()
tp.shape('square')
tp.speed('fastest')

def play_game():
    try:    
        font_size = 18

        upper_left_pos = -200
        tp.clear()
        tp.goto((0, 200))
        tp.write('Space Invaders!', move=False, align='center', font=("Cambria", font_size + 3, "bold"))
        
        # create a new player object
        player = Player()

        # listen for arrow key events and exit on ESC key
        ws.listen()
        ws.onkey(player.turn_left, "Left")
        ws.onkey(player.turn_right, "Right")
        ws.onkey(ws.bye, "Escape")

        game_is_on = True

        while game_is_on:
            time.sleep(0.1)
            ws.update()
            if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
                game_is_on = False
        
        ws.bye()
    except Exception as er:
        pass

def game_over():
    tp.clear()
    tp.goto((0, 0))
    tp.write('GAME OVER!', move=False, align="center", font=("Arial", 32, "normal"))
    tp.goto((0, -50))
    tp.write('Press (b) to return to main menu.', move=False, align="center", font=("Arial", 15, "italic"))
    turtle.listen()
    turtle.onkey(display_main_menu, 'b')
    ws.mainloop()
    tp.hideturtle()

def quit_game():
    try: 
        ws.bye()
    except Exception as err:
        pass

# initial interface 
def display_main_menu(): 

    font_size = 18

    upper_left_pos = -200
    tp.clear()
    tp.goto((0, 200))
    tp.write('Doing Space Invaders Game with Turtle Module', move=False, align='center', font=("Cambria", font_size + 3, "bold"))
    tp.goto((0, 50))
    tp.write('Press (s) to start.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.goto((0, 0))
    tp.write('Press (q) to quit.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.hideturtle()
    
    turtle.onkey(play_game, 's')
    turtle.onkey(quit_game, 'q')
    turtle.listen()
    ws.mainloop()
