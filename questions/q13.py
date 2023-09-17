"""
Explain method overloading and overriding in python
"""

class Person:
    name = "Ram"
    def description(self):
        return f"My name is {self.name}"

    def description(self, last_name):
        return f"My name is {self.name} {last_name}"

class Student(Person):
    def description(self):
        print(super().description("Sharma"))
        return "I study in grade 10"

s = Student()
print(s.description())