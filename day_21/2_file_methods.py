# There are some file methods which can useful in file handling projects

filename = "message.txt"
# read()
with open(filename, "r") as fp:
    data = fp.read(7)
print(data)


# seek()
# It changes the cursor position of the file pointer in the file
with open(filename, "r") as fp:
    fp.seek(13)
    data = fp.read()
    fp.seek(0)
    d = fp.read()
print(data)
print(d)


# readline()
with open(filename, "r") as fp:
    data = fp.readline()
    fp.seek(13)
    d = fp.readline()
print(data)
print(d)


# readlines()
with open(filename, "r") as fp:
    data = fp.readlines()
    print(fp.tell())  # tells the current cursor position in the file
print(data)  # ["Hello World\n", "I'm Learning Python\n", "Python is a high level langauge"]


data = ["HelloWorld\n", "I am Learning Python\n", "Python is a High Level Langauge"]
with open(filename, "w") as fp:
    fp.writelines(data)
