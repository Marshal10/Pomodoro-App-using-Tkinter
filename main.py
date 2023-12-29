from tkinter import *
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
window=Tk()
window.title("Pomodoro App")
window.config(padx=50,pady=50,bg=YELLOW)


label=Label(text="Timer",font=(FONT_NAME,50,"normal"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

canvas=Canvas(width=206,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
canvas_text=canvas.create_text(103,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
txt=canvas.itemcget(canvas_text,'text')
canvas.grid(column=1,row=1)

start_btn=Button(text="Start")
start_btn.grid(column=0,row=2)

reset_btn=Button(text="Reset")
reset_btn.grid(column=2,row=2)

checkmark=Label(text="✔",bg=YELLOW,fg=GREEN)
checkmark.grid(column=1,row=3)

window.mainloop()