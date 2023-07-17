from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2,2)
        self.setheading(90)        
        self.goto(0, -200)
        self.color("blue")
        self.missiles = [] 

    def turn_left(self):
        self.setheading(self.heading() + 5)
        

    def turn_right(self):
        self.setheading(self.heading() - 5)
        

    def create_missile (self):
        new_missile = Turtle()
        new_missile.penup()
        new_missile.goto(0, -200)
        new_missile.color("red")
        new_missile.setheading(self.heading())
        self.missiles.append(new_missile)
        
    def fire(self):
        for m in self.missiles:
            m.forward(10)