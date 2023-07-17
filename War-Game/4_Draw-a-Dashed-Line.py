from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("blue")

"Draw a Square"
for i in range (4):
    t.left(90)
    for i in range(20):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

"Draw a Triange"
for i in range (3):
    t.left(120)
    for i in range(20):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()



screen = Screen()
screen.exitonclick()


