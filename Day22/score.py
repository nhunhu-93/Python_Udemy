from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 25, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.score()
        self.hideturtle()
        
    def score(self):
        self.clear()
        self.setposition(-40,240)
        self.write(self.score_left,align=ALIGN, font=FONT)
        self.setposition(40,240)
        self.write(self.score_right,align=ALIGN, font=FONT)
        
    def increase_left(self):
        self.score_left += 1
        self.score()
        
    def increase_right(self):
        self.score_right += 1
        self.score()