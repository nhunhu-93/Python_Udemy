from tkinter import *

def click_button():
    guess_input = int(input.get())
    km = guess_input / (0.62137)
    result_label.config(text=f"{round(km,2)}")

window = Tk()
window.minsize(width = 180, height = 130)
window.title("Mile to KM converter")
window.config(padx= 30, pady= 30)

# Entry
input = Entry()
input.grid(column = 1, row = 0)

# Label
mile_label= Label(text="Miles")
mile_label.grid(column = 2, row = 0)

label2= Label(text="is equal to")
label2.grid(column = 0, row = 1)

result_label= Label(text="0")
result_label.grid(column = 1, row = 1)

km_label= Label(text="Km")
km_label.grid(column = 2, row = 1)

# Button
button = Button(text="Calculate", command=click_button)
button.grid(column = 1, row = 2)


window.mainloop()