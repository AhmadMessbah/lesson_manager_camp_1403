from tkinter import Tk, Button
import tkinter.messagebox as msg
from components import *
import controller.person_controller as p_control


def person_click():
    win_person = Toplevel(win)
    win_person.title("person")
    win_person.geometry("330x500")
    def refresh_person_side():
           p_id.variable.set("")
           p_name.variable.set("")
           p_family.variable.set("")
           p_grade.variable.set("")

           p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

    def person_select(row):
           p_id.variable.set(row[0])
           p_name.variable.set(row[1])
           p_family.variable.set(row[2])
           p_grade.variable.set(row[3])



    def p_save_click():
           status, message = p_control.save(
                  p_name.variable.get(),
                  p_family.variable.get(),
                  p_grade.variable.get())

           if status:
                  msg.showinfo("Save", message)
                  refresh_person_side()
           else:
                  msg.showerror("Save Error", message)

    def p_edit_click():
           status, message = p_control.edit(
                  p_id.variable.get(),
                  p_name.variable.get(),
                  p_family.variable.get(),
                  p_grade.variable.get())

           if status:
                  msg.showinfo("Edit", message)
                  refresh_person_side()
           else:
                  msg.showerror("Edit Error", message)

    def p_remove_click():
           status, message = p_control.remove(p_id.variable.get())

           if status:
                  msg.showinfo("Remove", message)
                  refresh_person_side()
           else:
                  msg.showerror("Remove Error", message)

    # Person
    Label(win_person, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
    p_id = TextAndLabel(win_person, "Id", 20, 50)
    p_name = TextAndLabel(win_person, "Name", 20, 85)
    p_family = TextAndLabel(win_person, "Family", 20, 120)
    p_grade = TextAndLabel(win_person, "grade", 20, 150)


    p_table = Table(win_person,
                    None,
                    ["id", "Name", "family" , "grade"],
                    [45, 100, 100,45],
                    20,
                    180,
                    person_select)
    Button(win_person, text="SavePerson", width=11, command=p_save_click).place(x=20, y=410)
    Button(win_person, text="EditPerson", width=11, command=p_edit_click).place(x=118, y=410)
    Button(win_person, text="RemovePerson", width=12, command=p_remove_click).place(x=218, y=410)

    refresh_person_side()





def lesson_click():
       new_window = Toplevel(win)
       new_window.title("پنجره جدید")
       label = Label(new_window, text="این پنجره جدید است!").pack()
def select_click():
    new_window = Toplevel(win)
    new_window.title("پنجره جدید")
    label = Label(new_window, text="این پنجره جدید است!").pack()



win = Tk()
win.title("Library")
win.geometry("310x200")
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
       command=select_click).place(x=162, y=60)



win.mainloop()
