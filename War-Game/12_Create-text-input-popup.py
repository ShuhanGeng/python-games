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

screen.setup(500, 300)
result = screen.textinput(title= "Caculate", prompt= "5*4=?")

print(result)



screen.exitonclick()

Screen().done()

