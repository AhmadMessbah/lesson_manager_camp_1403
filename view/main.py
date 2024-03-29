from tkinter import Tk, Button
import tkinter.messagebox as msg
from components import *
import controller.person_controller as p_control


def person_click():
    pass
def lesson_click():
    pass
def select_click():
    pass


win = Tk()
win.title("Library")
win.geometry("170x270")
Button(win,
       text="person",
       width=10,
       height=2,
       bg="lightblue",
       font=("Arial", 16),
       command=person_click).place(x=20, y=20)

Button(win,
       text="lesson",
       width=10,
       height=2,
       bg="lightgreen",
       font=("Arial", 16),
       command=lesson_click).place(x=20, y=100)

Button(win,
       text="lesson select",
       width=10,
       height=2,
       bg="lightyellow",
       font=("Arial", 16),
       command=select_click).place(x=20, y=180)



win.mainloop()
