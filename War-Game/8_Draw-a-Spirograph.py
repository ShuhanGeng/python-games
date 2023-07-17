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

# def drawCircle(angle):
#     for i in range(360//angle):
#         t1.color(random_color())
#         t1.circle(100)
#         t1.setheading(t1.heading() + angle)

# drawCircle(20)  

def draw(angle):
    for i in range(360//angle):
        t1.color(random_color())
        t1.forward(100)
        t1.left(90)
        t1.forward(100)
        t1.left(90)
        t1.forward(100)
        t1.left(90)
        t1.forward(100)
        t1.left(90)
        t1.setheading(t1.heading() + angle)

draw(1)        

screen = Screen()
screen.exitonclick()

Screen().done()

