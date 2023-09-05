# Polymorphism refers to many forms.
# In Python, it refers to different forms of functions and objects.
# len(), sum(), min(), max(), '+' operator, '-' operator etc. shows polymorphism in Python.

# In polymorphism, we mainly study about function/method overloading and operator overloading


# Function Overloading
# Function / method overloading occurs when a function with same name is defined multiple times
# Other OOP languages like C++, Java may support function / method overloading but Python doesn't
# support function overloading


# def addition(a, b):
#     return a + b

def addition(a, b, c=0):
    return a + b + c


r = addition(2, 3)  # Error
print(r)
r = addition(2, 3, 4)  # 9
print(r)


# We can give the taste of function overloading by using default arguments and *args and **kwargs in
# Python. But, we can't say Python supports function overloading

class Vehicle:
    category = 'petrol'
    def description(self):
        return f"Vehicle has {self.category} type"

    def description(self):
        return f"Vehicle engine is of {self.category} type"

v = Vehicle()
print(v.description())

# This example shows that, method overloading is also not possible in Python
