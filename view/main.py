from tkinter import Tk, Button
import tkinter.messagebox as msg
from components import *
import controller.person_controller as p_control


def person_click():
    win_person = Toplevel(win)
    win_person.title("person")
    win_person.geometry("280x400")
    def refresh_person_side():
           p_name.variable.set("")
           p_family.variable.set("")
           p_grade.variable.set("")

           p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

    def person_select(row):
           p_name.variable.set(row[0])
           p_family.variable.set(row[1])
           p_grade.variable.set(row[2])



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
                  p_name.variable.get(),
                  p_family.variable.get(),
                  p_grade.variable.get())

           if status:
                  msg.showinfo("Edit", message)
                  refresh_person_side()
           else:
                  msg.showerror("Edit Error", message)

    def p_remove_click():
           status, message = p_control.remove(p_name.variable.get())

           if status:
                  msg.showinfo("Remove", message)
                  refresh_person_side()
           else:
                  msg.showerror("Remove Error", message)

    # Person
    Label(win_person, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
    p_name = TextAndLabel(win_person, "Name", 20, 40)
    p_family = TextAndLabel(win_person, "Family", 20, 75)
    p_grade = TextAndLabel(win_person, "grade", 20, 105)


    p_table = Table(win_person,
                    None,
                    [ "Name", "family" , "grade"],
                    [100, 100,45],
                    20,
                    135,
                    person_select)
    Button(win_person, text="SavePerson", width=9, command=p_save_click).place(x=20, y=365)
    Button(win_person, text="EditPerson", width=9, command=p_edit_click).place(x=95, y=365)
    Button(win_person, text="RemovePerson", width=12, command=p_remove_click).place(x=173, y=365)

    refresh_person_side()


def lesson_click():
    win_lesson = Toplevel(win)
    win_lesson.title("lesson")
    win_lesson.geometry("380x400")

    def refresh_person_side():
        l_name.variable.set("")
        l_teacher.variable.set("")
        l_description.variable.set("")

        p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

    def person_select(row):
        l_name.variable.set(row[1])
        l_teacher.variable.set(row[2])
        l_description.variable.set(row[3])

    def p_save_click():
        status, message = p_control.save(
            l_name.variable.get(),
            l_teacher.variable.get(),
            l_description.variable.get())

        if status:
            msg.showinfo("Save", message)
            refresh_person_side()
        else:
            msg.showerror("Save Error", message)

    def p_edit_click():
        status, message = p_control.edit(
            l_name.variable.get(),
            l_teacher.variable.get(),
            l_description.variable.get())

        if status:
            msg.showinfo("Edit", message)
            refresh_person_side()
        else:
            msg.showerror("Edit Error", message)

    def p_remove_click():
        status, message = p_control.remove(l_name.variable.get())

        if status:
            msg.showinfo("Remove", message)
            refresh_person_side()
        else:
            msg.showerror("Remove Error", message)

    # lesson
    Label(win_lesson, text="lesson Info", font=("Arial", 16)).place(x=20, y=10)
    l_name = TextAndLabel(win_lesson, "Name", 20, 40)
    l_teacher = TextAndLabel(win_lesson, "teacher", 20, 75)
    l_description = TextAndLabel(win_lesson, "description", 20, 105)

    p_table = Table(win_lesson,
                    None,
                    ["Name", "teacher", "description"],
                    [100, 100, 130],
                    20,
                    135,
                    person_select)
    Button(win_lesson, text="SavePerson", width=11, command=p_save_click).place(x=20, y=365)
    Button(win_lesson, text="EditPerson", width=11, command=p_edit_click).place(x=118, y=365)
    Button(win_lesson, text="RemovePerson", width=12, command=p_remove_click).place(x=218, y=365)

    refresh_person_side()

    #new_window = Toplevel(win)
       #new_window.title("پنجره جدید")
       #label = Label(new_window, text="این پنجره جدید است!").pack()
def select_click():
    new_window = Toplevel(win)
    new_window.title("پنجره جدید")
    label = Label(new_window, text="این پنجره جدید است!").pack()



win = Tk()
win.title("choose leasson")
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
       text="choose lesson",
       width=11,
       height=2,
       bg="lightyellow",
       font=("Arial", 16),
       command=select_click).place(x=158, y=60)



win.mainloop()
