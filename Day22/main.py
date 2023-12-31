from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Tạo màn hình game
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Tắt chế độ vẽ tự động của turtle

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = Score()

# Nhận lệnh từ bàn phím
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # Làm game trì hoãn 0.1s
    ball.move()
    screen.update()
    
    # Phát hiện va chạm với tường
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
        
    # Phát hiện va chạm với paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Khi paddle phải bị trượt bóng
    if ball.xcor() > 390:
        ball.reset_ball()
        score.increase_left()
        
    # Khi paddle trái bị trượt bóng
    if ball.xcor() < -390:
        ball.reset_ball()
        score.increase_right()

screen.exitonclick()