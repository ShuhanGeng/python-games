from turtle import Turtle, Screen, colormode
import random
import time


screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

screen.setup(600, 600)

we = Turtle()
enemy = Turtle()
we.penup()
enemy.penup()
we.shape("turtle")
enemy.shape("turtle")
we.color("blue")
enemy.color("red")
we.goto(-200, 0)
enemy.goto(200, 0)
enemy.setheading(enemy.heading() + 180)
our_life = 100
enemy_life = 100
we.write(f"{our_life}", font=("Arial", 20, "normal"))
enemy.write(f"{enemy_life}", font=("Arial", 20, "normal"))

def attack():
    global enemy_life
    global our_life
    we.goto(200, 0)
    time.sleep(1)
    enemy_life -= random.randint(10, 30)
    enemy.clear()
    enemy.write(f"{enemy_life}", font=("Arial", 20, "normal"))
    we.goto(-200, 0)
    time.sleep(1)
    enemy.goto(-200, 0)
    our_life -= random.randint(10, 30)
    we.clear()
    we.write(f"{our_life}", font=("Arial", 20, "normal"))
    enemy.goto(200, 0)
    if our_life <= 0:
        we.clear()
        we.write("We lose!", font=("Arial", 20, "normal"))
    if enemy_life <= 0:
        we.clear()
        we.write("We won!", font=("Arial", 20, "normal"))

screen.listen()
screen.onkey(key = "space", fun=attack)


screen.exitonclick()
