from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("pink")

colors = ["burlywood", "thistle", "light salmon", "medium slate blue", "aquamarine",
          "medium spring green", "hot pink","dark slate blue"]

## Vẽ hình vuông
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

## Vẽ đường đứt khúc
# for i in range(4):
#     tim.forward(10)
#     tim.penup() # ko vẽ được khi di chuyển
#     tim.forward(10)
#     tim.pendown() # vẽ được khi di chuyển

## Vẽ các hình tam giác, hình vuông,...liên tục
# def draw_shape(num_size):
#     angle = 360 / num_size
#     for i in range(num_size):
#         tim.forward(100)
#         tim.right(angle)

# for i in range(3,8):
#     tim.color(random.choice(colors))
#     draw_shape(i)


## Cho rùa đi 1 khoảng cách cố định theo hướng bất kỳ
directions = [0,90,180,270]
tim.speed("fast")
tim.pensize(10) # width của bút vẽ

for i in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    ## setheading: di chuyển theo số tương ứng với 4 hướng

screen = Screen()
screen.exitonclick()