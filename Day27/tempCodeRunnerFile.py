from tkinter import *

def button_click():
    my_label.config(text=f"History\n{input.get()}")

window = Tk()
window.title("My dudu")
window.minsize(width= 500, height= 400)

# label
my_label = Label(text="Welcome", font=("Ariel",24))
my_label.grid(colum = 0, row=0)

# Cách để thay đổi text trong label
# my_label["text"] = "Replace"
# my_label.config(text="Replace")

# Button
button = Button(text="Click me",command= button_click)
button.grid(colum = 1, row=1)

# Entry
input = Entry()
input.grid(colum = 2, row=2)


window.mainloop()