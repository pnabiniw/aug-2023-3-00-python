# String formatting in Python can be done with three methods
# 1. f-strings
# 2. format specifier
# 3. .format() method


# f-strings
name = "Jon"
message = f"Hello I'm {name}"
print(message)  # Hello I'm Jon


# .format() method
name = "Jane"
language = "Python"
message = "Hello I'm {}. I'm learning {}".format(name, language)
print(message)


# format specifier
name = "Jane"
language = "Python"
age = 21
message = "Hello I'm %s. I'm learning %s. I'm %d" % (name, language, age)
print(message)
