# Spec

- 2nd gen pomodor timer
- Work and break setter
- Current session tracker
- Uptime calc
- Custom alert sound

Process flow
- window opens:
    - day and date at the top
    - input box underneath and to the right of day and date. it will take positive integer hours, minutes and seconds as input
    - ledger underneath and to the left of day and date. Title "ledger". Two columns.
    - "start block" and "stark break" buttons underneath the input box
    - "End session" button at the bottom right underneath the ledger.
    - entry into ledger "Session start | currenttime(24 hour format, system time)"
- when user enters time into input box and clicks "start block":
    - ledger appended with "Block n | currenttime", where n is the block count for that session, starting at 1.
    - Timer display in input box starts counting down in 1second increments.
    - when timer display reaches zero:
        - display message saying "block complete"
        - play alert sound
- when user enters time into input box and clicks "start break":
    - ledger appended with "Break n | currenttime", where n is the break count for that session, starting at 1.
    - Timer display in input box starts counting down in 1second increments.
    - when timer display reaches zero:
        - display message saying "break complete"
        - play alert sound
- When the user presses the End session button:
    -   "Session end | currenttime" appended to the ledger
    - if possible, a basic log file of this could be updated/generated, that would be cool. each update in the log file would need to have the date appended it in a 3rd column on a row by row basis. this would allow for effective time use analysis. The long term could be that this tool creates a log of your work. making this an internet tool and allowing others to log their work as well would be neat. beyond the current scope of this current version though.
    

    