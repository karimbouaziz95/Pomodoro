import tkinter as tk

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

#######         Main Window         #######
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#######         Tomato Image         #######
canvas = tk.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_image)
canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

#######         Timer Label         #######
timer_label = tk.Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

#######         Start button         #######
start_button = tk.Button(text="Start", bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)


#######         Reset button         #######
reset_button = tk.Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

#######         Check mark Label         #######
timer_label = tk.Label(text="✓", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=3, column=1)



#######         Program main loop         #######
window.mainloop()