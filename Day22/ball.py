from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10 # Tốc độ di chuyển theo trục x
        self.y_move = 10 # Tốc độ di chuyển theo trục y
        self.move_speed = 0.1 # Tốc độ di chuyển của bóng
        
    # di chuyển bóng
    def move(self):
        x_cor = self.xcor()+ self.x_move
        y_cor = self.ycor()+ self.y_move
        self.goto(x_cor,y_cor)
        
    # bóng nẩy lại theo chiều dọc
    def bounce_y(self):
        self.y_move *= -1
        
    # bóng nẩy lại theo chiều ngang
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    # Đưa bóng về vị trí ban đầu
    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()
    