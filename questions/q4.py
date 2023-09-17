"""
1. What are the methods to get keys, values and key-value pair in dictionary?
2. How to loop in key-value pair?

"""

student = {"name": "ram", "age": 30}
print(student.keys())  # dict_keys(["name", "age"])
print(student.values())  # dict_values(["ram", 30])
print(student.items())

# [("name", "ram"), ("age": 30)]


for key, value in student.items():
    print(key)  # "name"
    print(value)  # "ram"

key, value = ("name", "ram")
