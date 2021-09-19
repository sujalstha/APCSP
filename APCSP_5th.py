import tkinter
from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#F98B88")

font = ("Arial" , 16)

AP_Student = []

progress = Progressbar(win, orient=HORIZONTAL,
                       length=200, mode='determinate')

class_code = tkinter.Label(win, text="Class Code: H73JO",
                           bg='#F98B88',
                           fg='white',
                           font=font,)


def progress_bar():
    import time
    starting_point = 1

    while starting_point < 110:
        progress['value'] = starting_point

        starting_point += 1.5
        win.update_idletasks()

        time.sleep(.1)

    if starting_point >= 110.5 or starting_point >= 110:
        class_code.pack(pady=15)
    else:
        pass


progress.pack(pady=10)

start_button = tkinter.Button(win, text="Join Class",
                              bg='#FFCBA4',
                              fg='white',
                              command=progress_bar).pack(pady=10)

mainloop()
