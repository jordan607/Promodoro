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
TICK = "✔"
reps = 0
timer_clock =None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    global reps
    reps = 0
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer, text="00:00")
    tomato_label.config(text = "Timer")
    tick_label.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_time = WORK_MIN * 60
    shortbreak_time = SHORT_BREAK_MIN * 60
    longbreak_time = LONG_BREAK_MIN *60
    global reps
    reps += 1
    if reps % 2 != 0:
        count_time(work_time)
        tomato_label.config(text = "Work", fg = PINK)
    elif reps == 8:
        count_time(longbreak_time)
        tomato_label.config(text="Break", fg = RED)
    elif reps % 2==0:
        count_time(shortbreak_time)
        tomato_label.config(text="Break" ,fg = YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_time(count):
    minutes_count = math.floor(count / 60)
    second_count = count % 60
    if second_count <= 10:
        second_count = f"0{second_count}"
    canvas.itemconfig(timer, text=f"{minutes_count}:{second_count}")
    if count > 0:
        global  timer_clock
        timer_clock = window.after(1000, count_time, count-1)
    else :
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks+=TICK
        tick_label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady= 50, bg = GREEN)

tomato_label = Label(text = "Timer", font = (FONT_NAME, 50, "bold"), fg = RED , bg =GREEN)
tomato_label.grid(row =1, column = 2)

canvas = Canvas(width = 200, height = 224, bg = GREEN, highlightthickness = 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
timer = canvas.create_text(100,130, text= "00:00", fill= "white", font = (FONT_NAME, 24, "bold"))
canvas.grid(row = 2, column = 2)

start_button = Button(text="Start", command= start_timer)
start_button.grid(row = 3, column = 1)

end_button = Button(text="Reset", command = reset_timer)
end_button.grid(row = 3, column = 3)


tick_label = Label(text = "", fg = RED , bg = GREEN)
tick_label.grid(row =4 , column = 2 )

window.mainloop()