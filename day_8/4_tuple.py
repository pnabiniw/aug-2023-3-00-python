# Tuple is an immutable datatype in Python
# Tuple can take different datatypes regardless they are mutable or immutable
# Indexing and Slicing in tuple is same as that of List
# Tuple elements are enclosed with parenthesis i.e. ()

# Creating an empty tuple
t = tuple()
t = ()

# Creating non-empty tuple
t = (1, 1.1, [1, 2, 3])
print(t)  # (1, 1.1, [1, 2, 3])


######### Accessing Tuple Elelements #############
# Tuple elements are accessed using indexing and slicing

vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # "a"
print(vowels[4])  # "u"
print(vowels[-1])  # "u"
print(vowels[-3])  # "i"
# print(vowels[-10])  # IndexError
# print(vowels[20])  # IndexError


data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

print(data[0:7])  # (a", "b", "c", "d", "e", "f", "g")
print(data[:5])  # ("a", "b", "c", "d", "e")
print(data[6:])  # ("g", "h", "i", "j")
print(data[3: 8])  # ("d", "e", "f", "g", "h")
print(data[6: 2])  # ()
print(data[6: -2])  # ("g", "h")
print(data[-8: -3])  # ("c", "d", "e", "f", "g")
print(data[-9: 8])  # ("b", "c", "d", "e", "f", "g", "h")
print(data[-3: -7])  # ()
print(data[2: 8: 2])  # ("c", "e", "g")
print(data[-9: -2: 2])  # ("b", "d", "f", "h")
