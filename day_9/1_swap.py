a = 1
b = 2
print(a)  # 1
print(b)  # 2

c = a
a = b
b = c
print(a)  # 2
print(b)  # 1


# Swapping using tuple packing and unpacking
a, b = b, a
