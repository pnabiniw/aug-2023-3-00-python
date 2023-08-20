# Methods are also functions but methods are the functions inside a class
# Methods must be called with object

def addition(a, b):  # Function definition
    return a + b

# here addition is just a function but not a method
result = addition(2, 3)   # function call
print(result)  # 5


class Student:
    def get_age_after_10_years(self, current_age):
        return current_age + 10

student = Student()
result = student.get_age_after_10_years(21)
print(result)  # 31
# Here get_age_after_10_years() is a method



############ List Methods #######################
# 1. append()
vowels = ["a", "e", "i", "o"]
vowels.append("u")
print(vowels)  # ["a", "e", "i", "o", "u]


# 2. extend()
data = [1, 2, 3]
result = data.extend([4, 5, 6])
print(result)  # None
print(data)  # [1, 2, 3, 4, 5, 6]


# 3. insert()
vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")
print(vowels)  # ["a", "e", "i", "o", "u"]


# 4. remove()
vowels = ["a", "e", "i", "o", "u"]
vowels.remove("o")
print(vowels)  # ["a", "e", "i", "u"]

# vowels.remove("z")  # This raises error: ValueError

# 5. pop()
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop()
print(result)  # u
print(vowels)  # ["a", "e", "i", "o"]

result = vowels.pop(1)  # we can also give index as a parameter
print(result)  # e
print(vowels)  # ["a", "i", "o"]


# clear()
vowels.clear()
print(vowels)  # []


# index()
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("e")
print(vowels)  # ["a", "e", "i", "o", "u"]
print(result)  # 1

# count()
data = [1, 2, 1, 2, 2, 5, 4, 4, 5]
result = data.count(2)
print(result)  # 3


list