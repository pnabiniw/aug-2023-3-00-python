# OOP is an approach of programming in which programs are modelled in the real world problems
# OOP stands for Object-Oriented Programming
# It has two major aspects; Class and Objects
# Class is the blueprint of an object. It has its own attributes known as properties and methods
# Objects are the instance of a class

# There are four major pillars of OOP
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction


class Vehicle:  # creating a class using "class" keyword
    engine_type = "petrol"  # class attribute

    def __init__(self, number_of_doors, color):  # the constructor
        self.number_of_doors = number_of_doors  # instance attribute
        self.color = color  # instance attribute

    def description(self):  # a method
        return f"The vehicle has {self.number_of_doors} doors and {self.color} color. It's engine is " \
               f"{self.engine_type} type"


v1 = Vehicle(4, 'green')   # Creating an object / instantiating an  object
print(v1.engine_type)  # objects can access the property and methods of the class using dot (.)

# We can also access the class attribute using the class.
print(Vehicle.engine_type)  # Petrol. This is termed as 'getting'

v1.engine_type = "diesel"  # This is termed as "setting"
print(Vehicle.engine_type)  # petrol
print(v1.engine_type)   # diesel


# __init__() function inside a class is called when the object of the class is created. So, this
# function is also called as a constructor
# print(Vehicle.color)   # it raises attribute error because color is not a class attribute it is an
# instance attribute

print(v1.color)  # green
print(v1.number_of_doors)  # 4


bike = Vehicle(number_of_doors=0, color="red")
print(bike.engine_type)  # petrol
print(bike.number_of_doors)  # 0
print(bike.color)  # red

bike.color = "yellow"
print(bike.color)  # yellow

# A method is a function defined inside the class. Methods are called with the class object. They can't
# be called independently. Here "description" is a method (function defined inside the class)
print(bike.description())
