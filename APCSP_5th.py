import tkinter
from tkinter import *
from tkinter.ttk import *
import tkfontchooser

win = Tk()
win.resizable(width=False, height=False)
win.title("AP Computer Science A")
win.geometry("500x300")
win.configure(bg="#F98B88")
background_image = PhotoImage(file="6ei2kv.png")

AP_Student = []  # Student List


def student_win():
    new_win = Toplevel(win)
    new_win.geometry("550x300")
    new_win.configure(bg="#89C950")
    new_win.title("Student| APCS A")

    students = Text(new_win, height=20,
                    width=len(max(AP_Student, key=len)),
                    bg="#89C950",
                    fg="black")

    for x in AP_Student:
        students.insert(END, '{student}\n'.format(student=x))

    students.pack()

    new_win.mainloop()


def add_student():
    INPUT = inputtxt.get("1.0", "end-1c")
    str(INPUT)
    AP_Student.append(INPUT)
    print(AP_Student)


# place background image into a label
place_bg = Label(win, image=background_image).place(x=0, y=0)

font = tkfontchooser.Font(family="Times", size=12, weight="bold")

progress = Progressbar(win, orient=HORIZONTAL,
                       length=200, mode='determinate')

class_code = tkinter.Label(win, text="Class Code: H73JO",
                           bg='black',
                           fg='white',
                           font=("Times", 15, "bold"))

students_check = tkinter.Button(win, text="Students",
                        bg='black',
                        fg='white',
                        font=font,
                        command=student_win)

inputtxt = Text(win, bg="white", height=1,
                width=15)

add_student = tkinter.Button(win, text="Add Student",
                     bg='black',
                     fg='white',
                     font=font,
                     command=add_student)


def progress_bar():
    import time
    starting_point = 0

    while starting_point <= 110:
        progress['value'] = starting_point
        starting_point += 10
        win.update_idletasks()
        time.sleep(.5)

    if starting_point >= 110:
        class_code.pack(pady=10)
        inputtxt.pack(pady=15)
        add_student.pack()
        students_check.pack()
    else:
        pass


progress.pack(pady=10)

start_button = tkinter.Button(win, text="Join Class",
                              bg='black',
                              fg='white',
                              font=font,
                              width=15,
                              height=2,
                              command=progress_bar).pack(pady=10)

mainloop()
