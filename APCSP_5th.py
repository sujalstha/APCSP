import tkinter
from tkinter import *
from tkinter.ttk import *
import time

win = Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#F98B88")

AP_Student = []

progress = Progressbar(win, orient=HORIZONTAL,
                       length=200, mode='determinate')

starting_point = 0


def progress_bar():
    global starting_point

    while starting_point < 110:
        progress['value'] = starting_point

        starting_point += 10
        win.update_idletasks()

        time.sleep(.5)

    if starting_point >= 110:
        pass
    else:
        pass


progress.pack(pady=10)

start_button = tkinter.Button(win, text="Join Class",
                              bg='#FFCBA4',
                              fg='white',
                              command=progress_bar).pack(pady=10)

mainloop()
