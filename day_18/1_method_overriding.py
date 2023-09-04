# If a child class defines the same method that is already defined in the parent to add some
# extra functionality then it is called as method overriding

class Vehicle:
    def __init__(self, color, doors):
        self.color = color
        self.doors = doors

    def description(self):
        return f"color of the vehicle is {self.color} and it has {self.doors} doors"


class Bike(Vehicle):
    def __init__(self, engine_type, color, doors):   # Method Overriding
        self.engine_type = engine_type
        super().__init__(color, doors)

    def description(self):
        print(super().description())
        return f"Bike has {self.engine_type} engine"


b = Bike('fi', 'red', 0)
print(b.description())


# Here both the constructor and the description method are overriden in the child class Bike
