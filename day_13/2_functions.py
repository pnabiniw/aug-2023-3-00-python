# Functions are the block of reusable codes
# If the same logic is repeated at multiple places in your program then they can be created as a function
# Functions in python are created using 'def' keyword

# Funtion can be of different variations:
# 1. Without Argument Without Return
def message():
    print("Hello World")


# 2. With Argument But Without Return
def addition(a, b):
    print(a + b)


result = addition(2, 3)
print(result)


# 3. With Argument With Return
def add(a, b):
    return a + b


# 4. Without argument with return
def message():
    return "Hello World"

result = message()
print(result)  # Hello World
