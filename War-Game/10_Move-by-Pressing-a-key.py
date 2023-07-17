from turtle import Turtle, Screen, colormode
import random
t1 = Turtle()
colormode(255)
t1.shape("turtle")
t1.speed("fastest")
screen = Screen()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def move():
    t1.forward(10)
def move_lef():
    t1.left(90)
screen.listen()
screen.onkey(key= "space", fun =move)
screen.onkey(key= "l", fun =move_lef)







screen.exitonclick()

Screen().done()

