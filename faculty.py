# todo: implement auto save,,,
#  requires properties tracking (using @property/ @property.setter decorator)
#  could write a custom decorator with storage hooked-in
from storable import Storable

AUTO_SAVE = False


class Person(Storable):
    def __init__(self, name, birthday, national_id):
        self.name = name
        self.birthday = birthday
        self.NID = national_id

    def get_unique_id(self):
        return self.NID


class Employee(Person):
    def __init__(self, name, birthday, national_id, degree, department):
        super().__init__(name, birthday, national_id)
        self.emp_degree = degree
        self.emp_department = department


class Teacher(Person):
    def __init__(self, name, birthday, national_id, degree, department):
        super().__init__(name, birthday, national_id)
        self.tet_degree = degree
        self.tet_department = department


class Student(Person):
    def __init__(self, name: str, birthday, national_id: str, number, department: str):
        super().__init__(name, birthday, national_id)
        self.std_number = number
        self.std_department = department
