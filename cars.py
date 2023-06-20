from turtle import Turtle
import random
color_list=["medium blue","dark blue","dark green",
            "spring green","deep sky blue","crimson","indigo",
            "medium purple","rosy brown", "gold"
            ]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.setheading(180)
        self.color(random.choice(color_list))
        self.goto(random.randint(90,180),random.randint(-225,240))

    def car_move(self,level):
        self.forward(20*level)