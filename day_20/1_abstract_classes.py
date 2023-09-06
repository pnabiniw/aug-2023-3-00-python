# Abstract Classes are those classes which can't be instantiated
# We can't create object of an abstract class
# These classes or only meant for the inheritance purpose
from abc import ABC, abstractmethod


class Animal(ABC):
    @staticmethod
    def sleep():
        return "I sleep at night"

    @abstractmethod
    def sound(self):
        pass


class Cow(Animal):
    def sound(self):
        return "I moo !!"


c = Cow()
print(c.sleep())
print(c.sound())


class Dog(Animal):
    def sound(self):
        return "I bark !!"


d = Dog()
print(d.sound())
