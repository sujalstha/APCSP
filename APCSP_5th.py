import tkinter
from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("AP Computer Science A")
win.geometry("550x300")
win.configure(bg="#F98B88")
background_image = PhotoImage(file="daniele-levis-pelusi-5x-pmgg6ioo-unsplash.jpg")

# place background image into a label
place_bg = Label( win, image=background_image).place(x=0, y=0)

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
    starting_point = 0

    while starting_point <= 110:
        progress['value'] = starting_point

        starting_point += 10
        win.update_idletasks()

        time.sleep(.5)

    if starting_point >= 110:
        class_code.pack(pady=15)
    else:
        pass


progress.pack(pady=10)

start_button = tkinter.Button(win, text="Join Class",
                              bg='#FFCBA4',
                              fg='black',
                              width=15,
                              height= 2,
                              command=progress_bar).pack(pady=10)

mainloop()
