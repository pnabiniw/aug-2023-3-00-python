# Class methods are those methods which take class as the first argument.
# It doesn't take "self" as a first parameter. It takes 'cls'
# Class methods can be useful in creating factory methods


# Class Method
class Person:
    def __init__(self, age):
        self.age = age

    @classmethod
    def age_from_year(cls, year):
        age = 2023 - year
        return cls(age)  # Person(31)

    @staticmethod
    def grade(current_grade):
        return f"I study in grade {current_grade}"


p1 = Person(25)
print(p1.age)  # 25

p2 = Person.age_from_year(1992)
print(p2.age)  # 31

print(p2.grade(10))  # I study in grade 10


# Here "age_from_year" method is a class method and such type of method is also called as a
# factory method


# Static Method
# Static Methods are those methods which do not change the state of the class or an object
# We do not pass self or cls in the static methods
# In the above Person class 'grade' is a static method

