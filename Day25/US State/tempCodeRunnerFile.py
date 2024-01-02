    for name in list_state:
        if input_name == name:
            row_name = data_state[data_state["state"] == name]
            
            new_turtle = Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(int(row_name.x), int(row_name.y))
            new_turtle.write(name)