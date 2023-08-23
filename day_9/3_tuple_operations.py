# Concatenation (+)
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)  # (1, 2, 3, 4, 5, 6)

# Repetition (*)
a = (1, 2)
print(a * 2)  # (1, 2, 1, 2)


# Membership Operation ('in' and 'not in')
a = (1, 2, 3)
print(2 in a)  # True
print(3 not in a)  # False


# Some functions that can be used with Tuple

a = (1, 2, 3, 4, 5)
print(sum(a))   # 15

print(max(a))  # 5
print(min(a))  # 1


a = (5, 2, 3, 1, 4)
result = sorted(a)
print(result)  # [1, 2, 3, 4, 5]


result = reversed(a)
print(list(result))  # [4, 1, 3, 2, 5]
