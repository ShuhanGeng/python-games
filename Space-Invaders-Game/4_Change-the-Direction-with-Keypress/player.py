from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(90)
        self.goto(0, -200)

    def turn_left(self):
        self.setheading(self.heading() + 5)

    def turn_right(self):
        self.setheading(self.heading() - 5)
