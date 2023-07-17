from turtle import Turtle

class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(2,2)
        self.setheading(90)
        self.goto(0, -200)
        self.color('blue')
