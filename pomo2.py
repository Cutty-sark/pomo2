#2nd gen desktop pomodoro timer
from tkinter import *
from tkinter import ttk
import time

def create_window():
    current_date = time.strftime("%A, %B %d, %Y")  
    root = Tk()
    root.title("Pomo2")
    frame1 = ttk.Frame(root, padding = 10)
    frame1.grid()
    ttk.Label(frame1, text=current_date).grid(column=1, row=0)
    root.mainloop()

def main():
    create_window()

if __name__ == "__main__":
    main()
