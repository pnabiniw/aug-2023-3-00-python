# Like any other language python also has its set of keywords. There are around 35 keywords in
# python.
# Keywords are the reserved words of the language which cannot be used as variables or any identifiers

help("keywords")


# Rules for naming identifiers

# 1. Identifiers are case-sensitive i.e in A = 1 and a = 1 , "A" and "a" are two different identifiers
# 2. Identifiers can not be the keywords
# 3. Identifiers can't start with numbers.
# 4. Identifiers can include from A-Z, a-z, 0-9 (but can't start with nums) and underscore (_)
# 5. Can't include special characters like (@, !, $ etc.)



############ Python Statement #####################
# Each line in a program is a python statement
# But sometimes multiple statements can be written in a same line and also one statement can occur
# in multiple lines

m1 = "hello"; m2 = "world"  # two statements in a single line
message = "Hello I'm learning Python. " \
          "Python is a high level language"  # single statement in two lines


################### Indentations in Python ###########################
# Indentations in python are very important. They are the part of syntax
# Indentation helps to define a block of code in python

a = 1
if a > 2:
    print("Hello World")


############# Comments in Python ##############
# hash (#) in python is used as a single line comment
# triple-quoted string ("""""") in python can be used as a multiline comment

"""
These are multiline comments using triple-quoted string
"""

