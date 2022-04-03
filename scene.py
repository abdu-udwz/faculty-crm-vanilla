import tkinter as tk
import controller


class Scene(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text='Name').grid(row=0)
        name_field = tk.Entry(self)
        name_field.grid(row=0, column=1, columnspan=3)
        self.name_field = name_field

        add_student_btn = tk.Button(self, text='New student', command=self.on_add_student)
        add_student_btn.grid(row=1, column=0, pady=1)

        add_employee_btn = tk.Button(self, text='New employee', command=self.on_add_employee)
        add_employee_btn.grid(row=1, column=1, pady=1)

        add_teacher_btn = tk.Button(self, text='New teacher', command=self.on_add_teacher)
        add_teacher_btn.grid(row=1, column=2, pady=1)

    def on_add_student(self):
        # update user interface
        controller.create_student(self.name_field.get())

    def on_add_employee(self):
        pass

    def on_add_teacher(self):
        pass
