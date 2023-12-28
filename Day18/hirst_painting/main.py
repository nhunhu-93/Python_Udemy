## Trích xuất màu từ hình ảnh bằng colorgram
# import colorgram

# colors_list = []
# colors = colorgram.extract('Day18/hirst_painting/image.jpg', 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,b,g)
#     colors_list.append(new_color)
    
# print(colors_list)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

colors_lists = [(250, 247, 249), (243, 250, 246), (244, 248, 251), (252, 248, 244), (219, 107, 153),
                (133, 195, 171), (222, 88, 72), (215, 149, 131), (24, 152, 119), (241, 98, 208), (121, 149, 177),
                (38, 84, 119), (20, 204, 165), (219, 76, 83), (140, 62, 86), (131, 102, 83), (175, 215, 185),
                (21, 123, 168), (161, 166, 209), (174, 74, 154), (3, 115, 96), (237, 174, 161), (238, 152, 166),
                (54, 93, 59), (152, 220, 207), (102, 174, 126), (40, 76, 56), (34, 53, 87), (232, 16, 209), (74, 40, 79)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

number_dot = 100
for dot_count in range(1, number_dot+1):
        tim.dot(20, random.choice(colors_lists))
        tim.forward(50)
        
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

screen = t.Screen()
screen.exitonclick()