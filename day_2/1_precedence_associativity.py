# Precedence is the order in which operations are carried out
# Multiple operators can have same precedence. In such cases, associativity is considered
# Normally associativity order is from left to right except for the case of **

a = 3 - 2 + 1
print(a)
# here 3-2 is first calculated and the result is added with 1


# But for '**' associativity is from right to left
a = 2**2**3
print(a)  # 256

