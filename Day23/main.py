import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Tắt chế độ vẽ tự động của turtle

turtle = Player()
car = CarManager()     
score = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1) # Làm game trì hoãn 0.1s
    screen.update() 
    
    car.create_car()
    car.move()
    
    # Phát hiện turtle va chạm với car
    for cars in car.list_car:
        if turtle.distance(cars) < 30:
            game_is_on = False
            score.end_game()
            
    # Khi turtle chạm vào góc trên màn hình
    if turtle.ycor() == 290:
        turtle.go_to_start()
        car.level_up()
        score.increase_score()

screen.exitonclick()
