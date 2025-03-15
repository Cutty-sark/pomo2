#2nd gen desktop pomodoro timer
from tkinter import *
from tkinter import ttk
import time

def create_window():
    root = Tk() # initiating root window
    root.title("Pomo2") # title of window
    
    #frame for date
    current_date = time.strftime("%A, %B %d, %Y")  
    framedate = ttk.Frame(root, padding = 10) # frame 1 for date
    framedate.grid() # frame will be populated using grid config
    ttk.Label(framedate, text=current_date).grid(column=0, row=0)
    
    #frame for inputs and timer display
    frametimer = ttk.Frame(root, padding=10)
    frametimer.grid()
    
    
    root.mainloop()

    

def main():
    create_window()

if __name__ == "__main__":
    main()
