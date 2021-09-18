import tkinter
from tkinter import *
from tkinter.ttk import *

win = tkinter.Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#89C950")

AP_Student = []


def progress_bar():
    pass


progress = Progressbar(win, orient=HORIZONTAL,
                       length=150, mode='determinate').pack(pady=10)

start_button = Button(win, text="Join Class",
                      command=progress_bar).pack(padx=10)

win.mainloop()
