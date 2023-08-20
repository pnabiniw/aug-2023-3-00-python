# Strings are the immutable datatype in Python
# They are also sequential types like list. So, indexing and slicing are possible
# in the string

# Creating an empty string
a = str()  # empty string
a = ""  # empty string

# Creating non-empty strings
message = "Hello World"  # using double-quotes
message = 'Hello World.' \
          'I am learning Python'  # using single quote
message = """
Hello World
I am learning Python
"""   # using triple-quotes


message = "I'm learning Python"
message = 'He said, "Python is a high level language"'

message = 'I\'m learning Python'
message = "He said, \"Python is a high level language\""
print(message)


# Escape characters
# \", \', \n, \t etc are the escape characters
message = "Hello\nWorld"
print(message)
message = "Hello\tWorld"
print(message)

