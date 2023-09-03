"""
Create a class Person with instance attributes name and age.
Create a method get_details in this class to print name and age.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"


p1 = Person("Jon", 25)
print(p1.get_details())


class Employee(Person):
    salary = 20000
    designation = "teacher"

    def get_details(self):
        return f"Name is {self.name}. Age is {self.age}. Salary is {self.salary} and" \
               f"designation is {self.designation}"


e1 = Employee("Jon", 25)
print(e1.get_details())
