#2nd gen desktop pomodoro timer
from tkinter import *
from tkinter import ttk
import time

def create_window():
    root = Tk() # initiating root window
    root.title("Pomo2") # title of window

    #styling components
    style = ttk.Style()
    style.configure("Custom.TButton", font=("MS Mincho", 10))
    
    #frame for date
    current_date = time.strftime("%A, %B %d, %Y")  
    framedate = ttk.Frame(root, padding = 10) # frame 1 for date
    framedate.grid() # frame will be populated using grid config
    ttk.Label(framedate, text=current_date, font=("MS Mincho", 11)).grid(column=0, row=0)
    

    # Frame 2: Timer Input & Controls (Left)
    frametimer = ttk.Frame(root, padding=10,)
    frametimer.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Timer input fields
    ttk.Label(frametimer, text="Hours:", font=("MS Mincho", 11)).grid(row=0, column=0)
    hours_entry = Entry(frametimer, width=5)
    hours_entry.grid(row=0, column=1)

    ttk.Label(frametimer, text="Minutes:", font=("MS Mincho", 11)).grid(row=0, column=2)
    minutes_entry = Entry(frametimer, width=5)
    minutes_entry.grid(row=0, column=3)

    ttk.Label(frametimer, text="Seconds:", font=("MS Mincho", 11)).grid(row=0, column=4)
    seconds_entry = Entry(frametimer, width=5)
    seconds_entry.grid(row=0, column=5)

    # Block type entry
    block_type_entry = Entry(frametimer, width=20, font=("MS Mincho", 10))
    block_type_entry.grid(row=1, column=0, columnspan=6, pady=5)
    block_type_entry.insert(0, "Block Type")

    # Control buttons
    start_block_button = ttk.Button(frametimer, text="Start Block", style="Custom.TButton")
    start_block_button.grid(row=2, column=0, columnspan=3, pady=5)

    start_break_button = ttk.Button(frametimer, text="Start Break", style="Custom.TButton")
    start_break_button.grid(row=2, column=3, columnspan=3, pady=5)

    # Ledger & Session Tracking (Right)
    frameledger = ttk.Frame(root, padding=10)
    frameledger.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    ttk.Label(frameledger, text="Ledger", font=("MS Mincho", 11)).pack()
    ledger_display = Listbox(frameledger, width=40, height=10)
    ledger_display.pack()

    # End session button
    end_session_button = ttk.Button(frameledger, text="End Session", style="Custom.TButton")
    end_session_button.pack(pady=5)
    
    
    root.mainloop()

    

def main():
    create_window()

if __name__ == "__main__":
    main()
