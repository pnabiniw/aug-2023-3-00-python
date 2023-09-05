# Operator overloading refers to defining a function which is called when an operation is carried
# out using operators.
# In Python there are several magic methods of the respective operators which are invoked during an
# operation
# __add__(), __sub__(), __mul__(), __gt__() etc. are some of the magic methods which are called by
# '+', '-', '*', '>' operators respectively


a = 1  # int
b = 2  # int
print(a + b)  # 3

r = a.__add__(b)
print(r)  # 3


a = "Hello"
b = "World"
print(a + b)  # HelloWorld

print(a.__add__(b))  # HelloWorld

a = 1
b = "World"
print(a + b)  # TypeError

a.__add__(b)
