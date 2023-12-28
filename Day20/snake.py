from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.list_square = []
    
    
    def create_snake(self):
        for position in STARTING_POSITION:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.list_square.append(turtle)
            
    def move(self):
        for seg_num in range(len(self.list_square)-1, 0,-1):
            new_x = self.list_square[seg_num-1].xcor()
            new_y = self.list_square[seg_num-1].ycor()
            self.list_square[seg_num].goto(new_x, new_y)
    
        self.list_square[0].forward(20)
        self.list_square[0].left(90)