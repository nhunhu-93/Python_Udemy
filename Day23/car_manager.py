from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_car = []
        self.hideturtle()
        self.penup()

    def create_car(self):
        random_run = random.randint(1,6)
        if random_run == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid= 1, stretch_len= 1 * 2)
            new_car.penup()
            start_y = random.randint(-245, 245)
            new_car.setposition(300, start_y)
            self.list_car.append(new_car)
        
    def move(self):
        for car in self.list_car:
            car.backward(STARTING_MOVE_DISTANCE)
