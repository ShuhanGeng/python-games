from turtle import Turtle, Screen, colormode
import random

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

t1 = Turtle()

t1.shape("turtle")
t1.speed("fastest")
t1.hideturtle()
t1.penup()
for i in range(400):
    t1.dot(random.randint(1, 50), random_color())
    t1.goto(random.randint(-300, 300), random.randint(-300, 300))

screen = Screen()
screen.exitonclick()

Screen().done()

