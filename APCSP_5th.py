import tkinter
from tkinter import *
from tkinter.ttk import *

win = tkinter.Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#89C950")

AP_Student = []

progress = Progressbar(win, orient=HORIZONTAL,
                       length=150, mode='determinate').pack(pady=10)


def progress_bar():
    import time
    x = 0

    while x < 110:
        progress['value'] = x
        x += 8
        win.update_idletasks()
        time.sleep(.5)
    if x >= 100:
        pass
        # class_code.pack(pady=15)
        # inputtxt.pack(pady=25)
        # add_student.pack(pady=28)
        # students_check.pack()
    else:
        pass


start_button = Button(win, text="Join Class",
                      command=progress_bar).pack(pady=10)

mainloop()
