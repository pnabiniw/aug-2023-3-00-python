# We can access string elements using indexing and slicing which is similar
# to the list
# Forward indexing starts from 0 and reverse indexing from -1

# Indexing
message = "Hello World"
print(message[0])  # H
print(message[5])  # <space>
print(message[-1])  # d
print(message[-8])  # l
# print(message[20])  # Error
# print(message[-20])  # Error

# Slicing
message = "I am learning Python"
print(message[:6])  # 'I am l'
print(message[0:5])  # 'I am '
print(message[3: 8])  # 'm lea'
print(message[4:])  # ' learning Python'
print(message[7: 2])  # ''
print(message[-8:-2])  # 'g Pyth'
print(message[-6: -8])  # ''
print(message[3:-3])  # 'm learning Pyt'
print(message[9:-11])  # ''

print(message[3: 8: 2])  # 'mla'


# Creating the object (empty and non-empty)
# Accessing the elements  (Indexing / slicing/ accessing element using Key)
# Operations
# Methods
# Built-in Function


# message = "Hello"
# message[2] = "L"   # It is not possible because string is immutable
# print(message)

del message  # del is a keyword that deletes the object
