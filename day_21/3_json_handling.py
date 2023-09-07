# JSON stands for JavaScript Object Notation
# It is a file format which is mainly used for the communication between two or more entities like:
# communication between web frontend and backend, desktop app and backend etc.
# JSON file has the extension of .json

# Some rules for JSON file
# 1. JSON content is the key-value pair similar to the python dictionary
# 2. Unlike dictionary, JSON can't have single quotes in the key-value pair
# 3. Integer can't have quotes
# 4. Arrays can also be a JSON content


import json

filename = "students.json"
students = [
    {'name': 'Jon', "age": 30, "address": "KTM"},
    {"name": "Jane", "age": 35, "address": "PKR"},
]

with open(filename, "w") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)

with open(filename, "r") as fp:
    data = fp.read()
    data = json.loads(data)

print(data)
address = data[0]["address"]
print(address)  # KTM
