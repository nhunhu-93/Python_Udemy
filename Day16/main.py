# from turtle import Turtle, Screen

# turtle = Turtle() #Tạo đối tượng Turtle
# print(turtle)
# turtle.shape("turtle") #Thay đổi hình dạng của Turtle
# turtle.forward(100)

# my_screen = Screen() #Tạo đối tượng Screen
# print(my_screen.canvheight) #Lấy chiều cao của màn hình
# my_screen.exitonclick() #Khi click chuột vào màn hình thì màn hình sẽ tắt

#----
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("PokeMon Name", ["Pikachu","Squirlte","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = "l"

print(table)
