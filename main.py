import tkinter as tk
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    hack_label.config(text="")
    reps = 0
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    start_button.config(state="disabled")
    reps += 1
    #work_sec = WORK_MIN * 60
    #short_break_sec = SHORT_BREAK_MIN * 60
    #long_break_sec = LONG_BREAK_MIN * 60
    
    work_sec = 5
    short_break_sec = 2
    long_break_sec = 3
    
    if reps > 8:
        reps = 1
    
    if reps % 2 == 0:
        hack_label.config(text=hack_label["text"] + "✓")
    

    if reps%8 == 0:
        timer_label.config(text="Break", foreground=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        timer_label.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", foreground=GREEN)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    if count >= 0:
        global timer
        canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()



# ---------------------------- UI SETUP ------------------------------- #

#######         Main Window         #######
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#######         Tomato Image         #######
canvas = tk.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_image)
time_text = canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

#######         Timer Label         #######
timer_label = tk.Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

#######         Start button         #######
start_button = tk.Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_time)
start_button.grid(row=2, column=0)


#######         Reset button         #######
reset_button = tk.Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

#######         Check mark Label         #######
hack_label = tk.Label(text="", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
hack_label.grid(row=3, column=1)



#######         Program main loop         #######
window.mainloop()