from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    # Hiển thị điểm số
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        
    # Tăng điểm số
    def increase_score(self):
        self.score += 1
        self.update_score()
        
        
        
        