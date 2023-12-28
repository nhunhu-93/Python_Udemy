from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # thiết lập diện tích khung
# hiện màn hình nhập dữ liệu
user_bet = screen.textinput(title="Make your bot", prompt="Witch turtle will win the race? Enter a color: ")
color = ["red", "orange","yellow","green","blue","purple"]
all_turtle = []

distance = -80
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y= distance)
    all_turtle.append(new_turtle)
    distance += 30

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The turtle {win_color} is the winner")
            else:
                print(f"You've lose! The turtle {win_color} is the winner")
        
        turtle_distance = random.randint(0,10)
        turtle.forward(turtle_distance)

screen.exitonclick()