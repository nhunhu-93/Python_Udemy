from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        
        
        