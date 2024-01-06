from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60) # làm tròn về số nguyên gốc, vd 4.8 thành 4
    count_mili = count%60
    
    if count_mili < 10:
        count_mili = f"0{count_mili}"
    
    canvas.itemconfig(timer_text, text =f"{count_min}:{count_mili}")
    if count > 0:
        window.after(1000, count_down,count-1)
        
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg = YELLOW)

# Label
timer_label = Label(text = "Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness= 0)
timer_label.grid(column= 1, row= 0)

# Canvas
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0)
# highlightthickness : giúp canvas không bị khác màu với background
photo_image = PhotoImage(file= "Day28/tomato.png")
canvas.create_image(100, 112, image = photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column= 1, row= 1)

#button1
start_button = Button(text="Start", highlightthickness= 0, command=start_timer)
start_button.grid(column=0, row=2)

#button2
start_button = Button(text="Reset", highlightthickness= 0)
start_button.grid(column=2, row=2)

#Label
check_label = Label(text="✓", fg=GREEN, font=(FONT_NAME,15,"bold"), bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()