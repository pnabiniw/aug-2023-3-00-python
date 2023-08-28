# There are three types of arguments in Python function
# 1. Positional Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments


# 1. Positional Arguments
# These are the required arguments in a function
# Values for them most be passed as parameters during function call

def addition(a, b):  # Here a and b are positional arguments
    return a + b


r = addition(3, 2)
print(r)
r = addition(a=3, b=2)
print(r)
r = addition(b=2, a=3)
print(r)


# Default Arguments
def addition(a, b, c=10):  # Here c is a default argument
    return a + b + c


r = addition(3, 2)
print(r)  # 15
r = addition(3, 2, c=4)
print(r)  # 9
r = addition(b=3, a=9, c=7)
print(r)
