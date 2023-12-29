from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps=0
marks=''
reset_game=False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps,marks,reset_game
    reset_game=True
    reps=0
    marks=''
    label.config(text="Timer",fg=GREEN)
    checkmark.config(text=marks) 
    canvas.itemconfig(canvas_text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,reset_game
    reset_game=False
    reps+=1
    work_sec=math.floor(60*WORK_MIN)
    short_break_sec=math.floor(60*SHORT_BREAK_MIN)
    long_break_sec=math.floor(60*LONG_BREAK_MIN)
    
    if reps%4==0:
        count_down(long_break_sec)
        label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work",fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps,marks
    count_min=math.floor(count/60)
    count_secs=count%60
    if reset_game:
        return
    if count_secs<10:
        count_secs=f"0{count_secs}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_secs}")  
        
    if count>0:
        window.after(1000,count_down,count-1)
    else:
        if reps%2!=0:
            marks+='✔'
        checkmark.config(text=marks)  
        start_timer()
          
        
        
    
        
     
    
    
def min_countdown(secs,mins):
    if secs==0 and mins!=0:
        print("Condition satisfied")
        return True
    elif secs==0 and min==0:
        return False

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
canvas.grid(column=1,row=1)

start_btn=Button(text="Start",command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn=Button(text="Reset",command=reset)
reset_btn.grid(column=2,row=2)

checkmark=Label(text="",bg=YELLOW,fg=GREEN)
checkmark.grid(column=1,row=3)

window.mainloop()