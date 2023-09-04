# Encapsulation is the process of data hiding in the OOP approach of programming
# We can create public, private and protected members of a class in most of the OOP languages
# In Python, protected members are created using a single underscore, private members are created
# using a double underscore and public members do not contain any underscores

class Vehicle:
    __engine_type = "petrol"  # private member

    def __init__(self, color, doors):
        self._doors = doors   # protected member
        self.color = color  # public

    def _description(self):
        return f"Vehicle has {self._doors} doors and {self.color} color"

    @property
    def engine_type(self):
        return self.__engine_type

    def set_engine_type(self, e_type):
        self.__engine_type = e_type


class Bike(Vehicle):
    def description(self):
        return super()._description()


# Protected members are usually accessible to the child class in other programming languages
# But in Python, protected members are also accessible from outside the class. But, this is not
# recommended

b = Bike('red', 0)
print(b.description())
print(b.engine_type)

b.set_engine_type("Diesel")
print(b.engine_type)


# Private members are completely inaccessible from outside the class
# print(b.__engine_type)   # Attribute Error

# But there is still a tricky way in Python to access the private member
print(dir(b))
print(b._Vehicle__engine_type)  # Though __engine_type is a private attribute, it is still accessible
# from outside the class in _Vehicle__engine_type attribute. This is known as "name mangling"
