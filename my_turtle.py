from turtle import Turtle

class MyTurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red","green")
        self.penup()
        self.setheading(90)
        self.goto(0,-250)
    
    def move(self):
        self.forward(40)
