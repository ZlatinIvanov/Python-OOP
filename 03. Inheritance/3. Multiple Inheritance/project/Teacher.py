from project.Employee import Employee
from project.Person import Person


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."
