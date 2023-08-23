# Tuple is immutable datatype. So, we only have two methods in tuple count() and index()

# count()
a = (2, 5, 1, 1, 2, 2, 2, 3, 3, 5)
result = a.count(2)
print(result)  # 4


# index()
a = (2, 5, 1, 1, 2, 2, 2, 3, 3, 5)
result = a.index(2)
print(result)  # 0

result = a.index(2, 3, 8)  # 4. 2 is present at the 4th position in range 3 to 8


