# Dictionary values can be of any data type.
# But, there is a rule for dictionary keys that they must immutable.
# Dictionary Keys can not contain any mutable type directly or indirectly

data = {1: "Hello", 2: "World"}  # Valid
data = {2.1: [1, 2, 3], True: "Hello"}   # Valid
data = {(1, 2, 3): 1, (4, 5): 2}  # Valid

data = {([1, 2, 3], 2): "Hello", 2: "World"}  # Invalid
data = {[1, 2, 3]: "Hello", 2: "World"}  # Invalid

student = {"name": "Jon", "address": "KTM"}  # Valid


# Membership in Dictionary is observed in keys and not in values
student = {"name": "Jon", "address": "KTM"}
print("Jon" in student)  # False
print("name" in student)  # True
print("address" not in student)  # False
