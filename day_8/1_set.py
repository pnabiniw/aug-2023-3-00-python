# Set is a mutable datatype in Python. But, the elements of the set must be immutable
# Unlike list, set is unordered. So, indexing and slicing is not possible in Python
# In set {1, 2} is equal to {2, 1}

# Creating an empty set
s = set()
# s = {}  # This is not an empty set. It is an empty dictionary

# Creating a non-empty set
s = {1, 1.1, (1, 2), True}
print(s)

s1 = set([1, 2, 2, 3, 1, 1, 4, 2, 2])
print(s1)  # {1, 2, 3, 4}

# s = {1, [1, 2], 3}  # This is invalid set because it has list as an element which is mutable
# s = {1, 2, (1, 2, [3, 4])}  # This is also invalid because tuple has a mutable element
