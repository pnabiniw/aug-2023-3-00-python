# Like any other programming language python also has its own set of operators
# Operator are the symbols used to carry out mathematical and logical operations.
# Operators in python are:
# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Relational / Comparison Operators
# 4. Assignment Operator
# 5. Membership Operator
# 6. Identity Operator

############### Arithmetic Operators #########################
# Addition (+)
a = 1
b = 2
print(a + b)  # 3

# Subtraction (-)
a = 1
b = 2
print(a - b)  # -1

# Multiplication (*)
a = 5
b = 2
print(a * b)  # 10

# Division (/)
a = 4
b = 2
print(a / b)  # 2


# Raise to the power (**)
a = 2
print(a ** 3)  # 8


# Remainder / Modulus (%)
a = 4
b = 5
print(a % 2)  # 0
print(b % 2)  # 1


# floor division (//)
a = 3
print(a / 2)  # 1.5
print(a // 2)  # 1

a = -3
print(a / 2)  # -1.5
print(a // 2)  # -2


# Relational Operators
# >, <, ==, >=, <= != are the relational operators
# Results of relational operations are True / False

a = 5
b = 2
print(a > b)  # True
print(b > a)  # False
print(a < b)  # False
print(a == b)  # False
print(a != b)  # True


# Logical Operators
# and, or , not are the logical operators in python
# The results of logical operators are also True / False

a = 5
b = 3
c = 5

print(a == c or a == b)  # True
print(a == c and a == b)  # False
print(a != c or a == b)  # False
print(a == c and a != b)  # True

a = True
print(not a)  # False
a = 5
print(not a)  # False


# Assignment Operator
# "=" is the basic assignment operator
institute = "Broadway"  # here = is the assignment operator

a = 1
print(a)  # 1
a = a + 1
print(a)  # 2
a += 1  # a = a + 1
print(a)  # 3

a = 5
a *= 2
print(a)  # 10


# Membership Operator
# 'in' and 'not in' are the membership operator
# The result of membership operation is also True / False
print(2 in [1, 2, 3])  # True
print(3 not in [1, 2, 3])  # False
