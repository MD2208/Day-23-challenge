from turtle import Screen
import time
from my_turtle import MyTurtle
from cars import Car
from level import Level

my_screen = Screen()
my_screen.tracer(0)
my_screen.colormode(255)
my_screen.setup(width=600,height=600)

my_turtle = MyTurtle()
car_list = []
first_car= Car()
car_list.append(first_car)
current_level = Level()

my_screen.listen()
my_screen.onkey(my_turtle.move ,'Up')

is_game_on = True
number_of_loops=0
while is_game_on:
    #Randomly car generating
    if number_of_loops % 5 == 0:
        new_car = Car()
        car_list.append(new_car)
    for car in car_list:
        car.car_move((current_level.game_level)*0.5)
    
    #Detect car and turtle crash
    for car in car_list:
       if car.distance(my_turtle) < 20:
           is_game_on = False

    #Detect turtle reaches top edge

    if my_turtle.ycor() > 275:
        current_level.game_level+=1
        current_level.set_level()
        my_turtle.goto(0,-250)
    
    if len(car_list)>20:
        car_list = car_list[2:]

    my_screen.update()
    time.sleep(0.1)
    number_of_loops+=1

my_screen.exitonclick()