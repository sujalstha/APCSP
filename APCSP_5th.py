import tkinter
from tkinter import *
from tkinter.ttk import *
import time

win = tkinter.Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#89C950")

AP_Student = []

progress = Progressbar(win, orient=HORIZONTAL,
                       length=150, mode='determinate').pack(pady=10)

x = 0


def progress_bar():
    global x

    while x < 110:
        progress['value'] = x

        x += 8
        win.update_idletasks()

        time.sleep(.5)


start_button = Button(win, text="Join Class",
                      command=progress_bar).pack(pady=10)

mainloop()
