from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.grade_score = 1
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.score()
        self.hideturtle()
        
    def score(self):
        self.write(f"Level: {self.grade_score}", align="left", font=FONT)
        
    def increase_score(self):
        self.clear()
        self.grade_score += 1
        self.score()
        
    def end_game(self):
        self.goto(0,0)
        self.write("GAME_OVER", align="center", font=FONT)
        
        
