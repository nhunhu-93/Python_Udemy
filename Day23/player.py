from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90) # Đặt hướng của turtle lên trên
    
    # Di chuyển turtle lên trên
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    # Đưa turtle về vị trí ban đầu
    def go_to_start(self):
        self.goto(STARTING_POSITION)
