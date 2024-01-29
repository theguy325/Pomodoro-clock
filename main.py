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
reps = 0
clock_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(clock_timer)
    canvas.itemconfig(canvas_text, text=f"00:00")
    timer.config(text="Timer", fg=GREEN)
    reps = 0
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    global clock_timer
    mins = math.floor(num / 60)
    if mins < 10:
        mins = f"0{mins}"
    secs = num % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(canvas_text, text=f"{mins}:{secs}")
    if num > 0:
        clock_timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for each in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=100)
window.config(bg=YELLOW)
window.title("The Pomodoro")
timer = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=2)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=2)
pomo_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomo_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
start = Button(text="start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=1)
reset = Button(text="reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=3)
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=2)
window.mainloop()
