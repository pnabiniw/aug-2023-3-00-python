# Loops are used to perform a task repeatedly
# It helps to reduce the manual effort and automate the task
# There are two types of loops in Python
# 1. For Loop
# 2. While Loop


# 1. for loop
# for loops in Python is applied in the sequence of data (iterables).
# Example: list, tuple dictionary, range() function, iterator objects etc.

# for loop in different python data-types
vowels = ["a", "e", "i", "o", "u"]

# for(i=0;i<=len(vowels);i++){
# print(vowels[i])
# }

for each in vowels:
    print(each)  # a, e, i, o, u


# for loop in dictionary
student = {"name": "Jane", "age": 30, "address": "Kalanki"}

for each in student:
    print(each)  # name, age, address

print(student.keys())
for key in student.keys():
    print(key)   # name, age, address


values = student.values()
print(values)
for value in values:
    print(value)  # Jane, 30, Kalanki


print(student.items())  # dict_items([("name", "Jane"), ("age", 30), ("address", "Kalanki)])
for each in student.items():
    print(each)  # ("name", "Jane"), ("age", 30), ("address", "Kalanki)

for each in student.items():
    key = each[0]
    value = each[1]

for key, value in student.items():
    print(key)  # name, age, address
    print(value)  # Jane, 30, Kalanki


# range() function
# range() is a built-in python function to generate a sequence of numbers
# range can take upto 3 parameters, start, end and step-size

seq = range(0, 11)
print(seq)  # range() object

for i in range(0, 11):
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in range(11):
    print(i)  # We can omit start value. If start value is omitted then it starts from 0

for i in range(3, 8):
    print(i)  # 3, 4, 5, 6, 7

for i in range(2, 11, 2):
    print(i)  # 2, 4, 5, 6, 8, 10


# enumerate()
# enumerate() takes iterable / sequence datatype as a parameter
# enumerate() is also a builtin function in python which can provide the count of each iteration
vowels = ["a", "e", "i", "o", "u"]
print(list(enumerate(vowels)))  # [(0, "a"), (1, "e"), (2, "i"), (3, "o"), (4, "u")]

for index, value in enumerate(vowels):
    print(index)  # 0, 1, 2, 3, 4
    print(value)  # a, e, i, o, u


for count, value in enumerate(vowels, start=1):
    print(count)  # 1, 2, 3, 4, 5
    print(value)  # a, e, i, o, u

