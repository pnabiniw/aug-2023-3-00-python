"""
Take two numbers as input and add those numbers. Handle the possible exceptions.

"""

try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    result = num1 + num2
except ValueError:
    print("Please enter valid number")
else:
    print(result)
