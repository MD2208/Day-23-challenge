from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.game_level=1
        self.hideturtle()
        self.goto(-150,260)
        self.set_level()

    def set_level(self): 
        self.clear()   
        self.write(f"Level : {self.game_level}", align="center", font=("MS Sans Serif",20,"normal"))