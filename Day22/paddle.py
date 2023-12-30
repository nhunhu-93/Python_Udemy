from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, X_PADDLE, Y_PADDLE):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1*5)
        self.setposition(X_PADDLE,Y_PADDLE)
        self.speed("fastest")
        
    def up(self):
        self.goto(self.xcor(), self.ycor()+15)
        
    def down(self):
        self.goto(self.xcor(), self.ycor()-15)
        