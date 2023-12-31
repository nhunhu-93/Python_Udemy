from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snack game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# Hành động di chuyển con rắn
screen.listen() # sự kiện lắng nghe
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on: 
    # update screen
    screen.update()
    time.sleep(0.1) # giảm độ chậm của thời gian
    snake.move() 
    
    # Phát hiện va chạm với thức ăn
    if snake.head.distance(food) < 15:
        food.refresh() # tạo thức ăn mới
        snake.extend() # tăng độ dài con rắn
        score.increase_score() # tăng điểm
        
    # Phát hiện va chạm với tường
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        
    # Phát hiện va chạm với đuôi
    for segment in snake.list_square[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            
screen.exitonclick()
