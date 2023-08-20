# True and False are the boolean types in Python.
# True and False are also the keywords in Python

# Operations that give boolean type

a = 5
b = 10
c = 15

# relational operations
print(b > a)  # True
print(b != a)  # True
print(b < a)  # False
print(a == c)  # False


# Logical Operations
print(b > a and a == c)  # False
print(b > a or a == c)  # True
print(not True)  # False
print(not False)  # True
print(not a)  # False

# Membership Operation
print(2 in [1, 2, 3])  # True
print(3 not in [1, 2, 3])  # False


# Identity Operation
a = 1
print(a)
b = 1
print(b)
print(a == b)  # True
print(a is b)  # True
a = 42345274575485  # It is created in one memory location
b = 42345274575485  # But it is created in another memory location
print(a == b)  # True
print(a is b)  # False



# Concept of Truthy and Falsy

# Truthy
# All non-empty datatypes and non-zero numbers are truthy values
a = 12
b = 5.7
c = [1, 2]
d = (4, 5)
e = {1, 2}
f = {"name": "Jon"}
g = True
# All these datatypes are truthy datatypes
# We can check the truthiness of the data using bool function

print(bool(b))  # True


# Falsy
# All empty datatypes and zero are falsy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = False
h = None
print(bool(g))  # False


# Python booleans are the subclass of the integer class. That means True is 1 and False is 0
a = True
b = 3
print(a + b)  # 4
print(70 * False)  # 0
print(True + True)  # 2








