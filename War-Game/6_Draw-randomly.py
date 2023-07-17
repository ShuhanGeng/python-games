# from turtle import Turtle, Screen
import random
import turtle

t1 = turtle.Turtle()

t1.shape("turtle")
t1.color("blue")
t1.speed("fastest")

t2 = turtle.Turtle()

t2.shape("turtle")
t2.color("red")
t2.speed("fastest")

t3 = turtle.Turtle()

t3.shape("turtle")
t3.color("green")
t3.speed("fastest")

t4 = turtle.Turtle()

t4.shape("turtle")
t4.color("black")
t4.speed("fastest")

angle = [0, 90, 180, 270, 360]

for i in range(200):
    t1.forward(10)
    # t1.right(random.randint(0, 360))
    t1.right(random.choice(angle))
    t2.forward(10)
    # t2.right(random.randint(0, 360))
    t2.right(random.choice(angle))
    t3.forward(10)
    # t2.right(random.randint(0, 360))
    t3.right(random.choice(angle))
    t4.forward(10)
    # t2.right(random.randint(0, 360))
    t4.right(random.choice(angle))


screen = turtle.Screen()
screen.exitonclick()

turtle.done()

