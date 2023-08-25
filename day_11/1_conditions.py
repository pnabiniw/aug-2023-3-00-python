# Conditions are used to make logical decisions in a program
# There are four variations of conditions in Python
# 1. Simple if
# 2. if...else statement
# 3. if...elif...else statement
# 4. Nested if


# 1. Simple if
# if statement takes truthy or falsy value with it. If the value is truthy then the statement inside
# if block is executed else it is not executed
a = 5
b = 10
c = 15
d = 0

if b > a:
    print("b is greater than a")

if b:
    print("b is non-zero")

if d:
    print("d is non-zero")



# 2. if...else statement
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

if d:
    print("d is non-zero")
else:
    print("d is zero")


# 3. if...elif...else
if a > b:
    print("a is greater than b")
elif a > c:
    print("a is greater than c")
elif b > c:
    print("b is greater than c")
else:
    print("c is the greatest")


# 4. Nested if
if c > b:
    if c > a:
        print("c is the greatest")
    else:
        print("c is not be the greatest")
else:
    print("b is greater than c")
