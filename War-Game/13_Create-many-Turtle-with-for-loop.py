from turtle import Turtle, Screen, colormode
import random

colormode(255)

screen = Screen()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

screen.setup(600, 600)


for i in range(20):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(random_color())
    new_turtle.goto(random.randint(-300, 300), random.randint(-300, 300))    

screen.exitonclick()

Screen().done()

