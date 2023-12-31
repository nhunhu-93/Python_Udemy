from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day20-21/Snake game/high_score.txt") as file:
            self.high_score = int(file.read())
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
            with open("Day20-21/Snake game/high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    # Tăng điểm số
    def increase_score(self):
        self.score += 1
        self.update_score()
        
        
        
        