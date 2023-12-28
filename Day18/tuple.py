import turtle as t
import random

# # không thể thay đổi 1 tuple
# tuples = (1,4,7)

# # chuyển tuple thành list
# list(tuples)

### Ví dụ 1
tim = t.Turtle()
# tim.shape("turtle")
# t.colormode(255)

# def random_colors():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color

# ## Cho rùa đi 1 khoảng cách cố định theo hướng bất kỳ
# directions = [0,90,180,270]
# tim.speed("fast")
# tim.pensize(10) # width của bút vẽ

# for i in range(200):
#     tim.color(random_colors())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     ## setheading: di chuyển theo số tương ứng với 4 hướng


### Ví dụ 2
# Vẽ 1 hình tròn di chuyển 
tim.shape("arrow")
t.colormode(255)
tim.speed("fastest")

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_circle(size):
    for i in range(int(360/size)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading()+ size)
    
draw_circle(5)

screen = Screen()
screen.exitonclick()

