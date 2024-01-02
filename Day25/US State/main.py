from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()

screen.title("U.S State Game")
image = "Day25/US State/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_state = pandas.read_csv("Day25/US State/50_states.csv")
list_state = data_state["state"].to_list()
guess_state = []

while len(guess_state) < 50:
    input_name = screen.textinput(title="Guess the State", prompt="What's another State name?")
    
    for name in list_state:
        if input_name == name:
            guess_state.append(input_name)
            
            new_turtle = Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            row_name = data_state[data_state["state"] == name]
            new_turtle.goto(int(row_name.x), int(row_name.y))
            new_turtle.write(name)

screen.mainloop()

