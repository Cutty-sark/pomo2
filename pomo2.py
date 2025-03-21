from tkinter import *
from tkinter import ttk
import time
import threading

#sanitising inputs for timer
def validate_numeric_input(P):
    return P.isdigit() or P == ""


def validate_time_values():
    try:
        h = int(hours_entry.get())
        m = int(minutes_entry.get())
        s = int(seconds_entry.get())
        if not (0 <= h <= 24 and 0 <= m <= 60 and 0 <= s <= 60):
            raise ValueError
    except ValueError:
        hours_entry.delete(0, END)
        minutes_entry.delete(0, END)
        seconds_entry.delete(0, END)
        hours_entry.insert(0, "00")
        minutes_entry.insert(0, "00")
        seconds_entry.insert(0, "00")

#decreasing count properly
def countdown_timer(total_seconds):
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)

        # Update GUI
        hours_entry.delete(0, END)
        minutes_entry.delete(0, END)
        seconds_entry.delete(0, END)
        hours_entry.insert(0, f"{hrs:02}")
        minutes_entry.insert(0, f"{mins:02}")
        seconds_entry.insert(0, f"{secs:02}")

        time.sleep(1)  
        total_seconds -= 1

    # Had issue with 1 second remaining, so setting to zero "00:00:00"
    seconds_entry.insert(0, "00")

    # Alert when the timer reaches zero
    ledger_display.insert(END, "Complete")
    root.bell()  # Play a system alert sound


def start_block():

    global block_count

    # Validate and get time
    validate_time_values()
    h = int(hours_entry.get())
    m = int(minutes_entry.get())
    s = int(seconds_entry.get())

    #if nothing input don't start
    total_seconds = h * 3600 + m * 60 + s
    if total_seconds == 0:
        return  

    # Geting  block type (limit to 20 characters)
    block_type = block_type_entry.get().strip()[:20] or " - "

    # Add entry to ledger
    block_count += 1
    current_time = time.strftime("%H:%M:%S")
    ledger_display.insert(END, f"Block {block_count} | {block_type} | {current_time}")

    # Start countdown in a separate thread to prevent UI freeze
    threading.Thread(target=countdown_timer, args=(total_seconds,), daemon=True).start()


def start_break():
    global break_count

        # Validate and get time
    validate_time_values()
    h = int(hours_entry.get())
    m = int(minutes_entry.get())
    s = int(seconds_entry.get())

    total_seconds = h * 3600 + m * 60 + s
    if total_seconds == 0:
        return  # Don't start timer if all inputs are 0


    # Add entry to ledger
    break_count += 1
    current_time = time.strftime("%H:%M:%S")
    ledger_display.insert(END, f"Break {block_count} | {current_time}")

    # Start countdown in a separate thread to prevent UI freeze
    threading.Thread(target=countdown_timer, args=(total_seconds,), daemon=True).start()

    
# Root window
root = Tk()
root.title("Pomo2")

# Styling
style = ttk.Style()
style.configure("Custom.TButton", font=("MS Mincho", 10))

# Frame for date
current_date = time.strftime("%A, %B %d, %Y")
framedate = ttk.Frame(root, padding=10)
framedate.grid()
ttk.Label(framedate, text=current_date, font=("MS Mincho", 11)).grid(column=0, row=0)

# Frame for Timer Input & Controls
frametimer = ttk.Frame(root, padding=10)
frametimer.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Input validation
vcmd = (root.register(validate_numeric_input), "%P")

ttk.Label(frametimer, text="Hours:", font=("MS Mincho", 11)).grid(row=0, column=0)
hours_entry = Entry(frametimer, width=5, validate="key", validatecommand=vcmd)
hours_entry.grid(row=0, column=1)
hours_entry.insert(0, "00")

ttk.Label(frametimer, text="Minutes:", font=("MS Mincho", 11)).grid(row=0, column=2)
minutes_entry = Entry(frametimer, width=5, validate="key", validatecommand=vcmd)
minutes_entry.grid(row=0, column=3)
minutes_entry.insert(0, "00")

ttk.Label(frametimer, text="Seconds:", font=("MS Mincho", 11)).grid(row=0, column=4)
seconds_entry = Entry(frametimer, width=5, validate="key", validatecommand=vcmd)
seconds_entry.grid(row=0, column=5)
seconds_entry.insert(0, "00")

# Block type entry
block_type_entry = Entry(frametimer, width=20, font=("MS Mincho", 10))
block_type_entry.grid(row=1, column=0, columnspan=6, pady=5)
block_type_entry.insert(0, "Block Type")

# Control buttons
block_count = 0
start_block_button = ttk.Button(frametimer, text="Start Block", style="Custom.TButton", command=start_block)
start_block_button.grid(row=2, column=0, columnspan=3, pady=5)

break_count = 0
start_break_button = ttk.Button(frametimer, text="Start Break", style="Custom.TButton", command=start_break)
start_break_button.grid(row=2, column=3, columnspan=3, pady=5)

# Ledger Frame
frameledger = ttk.Frame(root, padding=10)
frameledger.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

ttk.Label(frameledger, text="Ledger", font=("MS Mincho", 11)).pack()
ledger_display = Listbox(frameledger, width=40, height=10)
ledger_display.pack()

# End session button
end_session_button = ttk.Button(frameledger, text="End Session", style="Custom.TButton")
end_session_button.pack(pady=5)

root.mainloop()