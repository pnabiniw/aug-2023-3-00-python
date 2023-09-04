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


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        self.salary = salary
        self.designation = designation
        super().__init__(name, age)

    def get_details(self):
        print(super().get_details())
        return f"Salary is {self.salary} and designation is {self.designation}"


e1 = Employee("Jon", 25, 20000, "teacher")
print(e1.get_details())
