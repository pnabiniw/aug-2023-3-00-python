# Errors in Python are handled using try...except.
# There can be several variations of try...except block

# try...except
try:
    num = int(input("Enter a number "))
except:
    print("Something Went Wrong !!")


# try...except but with error name mentioned
try:
    num = int(input("Enter a number "))
except ValueError:
    print("Something Went Wrong !!")


# try...except with multiple errors mentioned
try:
    num = int(input("Enter a number "))
except (ValueError, KeyError):
    print("Something Went Wrong !!")

# try...except chain
try:
    num = int(input("Enter a number "))
except ValueError:
    print("Please enter a number ")
except TypeError:
    print("Please carry out proper operation")
except ZeroDivisionError:
    print("Please do not divide by zero")


# try...except with Exception as e
try:
    num = int(input("Enter a number "))
except Exception as e:
    print(e)

# try..except...else
try:
    a = int(input("Enter a number "))
    b = int(input("Enter second number "))
except ValueError:
    print("Input a number, not character")
else:
    print(a)
    print(b)
    print(a + b)


# try...except...else....finally

fp = open("message.txt", "r")
try:
    data = fp.read()
    result = data + "World"
except TypeError:
    print("Carry out proper operation")
else:
    print(result)
finally:
    fp.close()


# 1. At first "try" block is executed
# 2. If error occurs from the "try" block then "except" block is executed
# 3. If exception doesn't occur in the "try" block then "else" block is executed
# 4. "finally" block is always executed (whether the error occurs or not)
