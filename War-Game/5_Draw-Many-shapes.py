from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("blue")

def draw(number):
    for i in range (number):
        t.left(360/number)
        for i in range(10):
            t.forward(5)
            t.penup()
            t.forward(5)
            t.pendown()

def main(sides_shape):
    for i in range(3, sides_shape+1):
        draw(i)

main(10)

screen = Screen()
screen.exitonclick()


