# removing elements from a dictionary

student = {"name": "Jon", "age": 30, "address": "KTM"}

# pop()
# It takes key as an argument
result = student.pop("age")
print(result)  # 30
print(student)  # {"name": "Jon", "address": "KTM"}
# student.pop("phone")  # It raises KeyError as "phone" is not present in the dict


#popitem()
student = {"name": "Jon", "age": 30, "address": "KTM"}
result = student.popitem()
print(result)  # ("address", "KTM")
print(student)  # {"name": "Jon", "age": 30}

#clear()
student = {"name": "Jon", "age": 30, "address": "KTM"}
student.clear()
print(student)  # {}

del student  # It deletes the student object
# print(student)  # NameError


# copy()
student = {"name": "Jon", "age": 30, "address": "KTM"}
student1 = student.copy()
print(student)  # {"name": "Jon", "age": 30, "address": "KTM"}
print(student1)  # {"name": "Jon", "age": 30, "address": "KTM"}


# get()
student = {"name": "Jon", "age": 30, "address": "KTM"}
name = student.get("name")
print(name)  # "Jon"
phone = student.get("phone")
print(phone)  # None
phone = student.get("phone", 989098987)
print(phone)  # 989098987
name = student.get("name", "Jane")
print(name)  # Jon


# keys()
student = {"name": "Jon", "age": 30, "address": "KTM"}
keys = student.keys()
print(keys)  # dict_keys(["name", "age", "address"])

# values()
values = student.values()
print(values)  # dict_values(["Jon", 30, "KTM"])

# items()
items = student.items()
print(items)  # dict_items([("name", "Jon"), ("age", 30), ("address": "KTM")])

items = list(student.items())  # [("name", "Jon"), ("age", 30), ("address": "KTM")]
key, value = items[0]
print(key)  # "name"
print(value) # "Jon"


# fromkeys()
y = {}
result = y.fromkeys([1, 2], "Hello")
print(y)  # {1: "Hello", 2: "Hello"}
print(result)  # {1: "Hello", 2: "Hello"}
result = y.fromkeys([1, 2])
print(result)  # {1: None, 2:None}


# setdefault()
student = {"name": "Jon", "age": 30, "address": "KTM"}
student.setdefault("phone", 9890989878)
print(student)
student.setdefault("name", "Jane")
student.setdefault("phone", 9890989879)
print(student)
