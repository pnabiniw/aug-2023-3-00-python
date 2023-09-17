# Namespaces determine the scope of the variables and objects in Python
# Namespaces is explained by LEGB rule (Local, Enclosed, Global, Builtin)
# There are 4 types of namespaces
# 1. Local Scope
# 2. Enclosed Scope
# 3. Global Scope
# 4. Built-in Scope


# Built-in Scope
# If the scope of package or object is all over the project then it is an object of built-in scope
# Example: Python built-in libraries like math, os, json etc.
# import math  # Built-in Scope


# Global Scope
# If the scope of the variable or object is limited to one python module then it has a global scope
# to that module
a = 12  # This variable 'a' is limited to this python file only


# Local Scope
# If the variable scope is limited to a function then it has local scope

a = 12  # global scope
def test_func(a):
    print(a)  # 2
    a = 20   # local scope
    print(a)  # 20

print(a)  # 12
test_func(2)
print(a)  # 12

a = 10
def test():
    global a
    print(a)  # 10
    a = 20
    print(a)  # 20

print(a) # 10
test()
print(a)  # 20





# Enclosed Scope
# If the scope of the variable or object is limited to a nested function then it has an enclosed scope

a = 12  # Global Scope
def outer_fxn():
    a = 20   # Local Scope
    def inner_fxn():
        a = 30   # Enclosed Scope
        print(a)
    inner_fxn()
    print(a)

print(a)
outer_fxn()
print(a)


# But, we have a "global" keyword which can define even a local variable as a global.

a = 20
def outer_function():
    global a
    a = 40
    def inner_function():
        a = 30
        print(a)  # 30
    inner_function()
    print(a)  # 40

print(a)  # 20
outer_function()
print(a)  # 40



# non-local keyword
a = 20
def outer_function():
    a = 40
    def inner_function():
        nonlocal a
        a = 30
        print(a)  # 30
    inner_function()
    print(a)  # 30


print(a)  # 20
outer_function()
print(a)  # 20
