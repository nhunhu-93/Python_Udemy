from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0
class Snake:
    def __init__(self):
        self.list_square = []
        self.create_snake()
        self.head = self.list_square[0]
    
    # Tạo rắn
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.list_square.append(turtle)
        
    def extend(self):
        self.add_segment(self.list_square[-1].position())
            
    #di chuyển từng phần của con rắn
    def move(self):
        for seg_num in range(len(self.list_square)-1, 0,-1):
            new_x = self.list_square[seg_num-1].xcor() # lấy tọa độ x của hình trước đó
            new_y = self.list_square[seg_num-1].ycor() # lấy tọa độ y của hình trước đó
            self.list_square[seg_num].goto(new_x, new_y) # đưa hình đến vị trí của hình trước đó
        self.head.forward(MOVE_DISTANCE) # di chuyển hình đầu tiên
        
    # Phương thức điều khiển di chuyển
    def up(self):
        if self.head.heading() != DOWN:  # lấy hướng hiện tại của đầu rắn
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)