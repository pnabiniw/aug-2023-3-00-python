# WAP to create a "login_required" decorator which if added to a function asks for a password. If the
# password is entered "123" then the function can be accessed else throw the message "Invalid Password"

def login_required(func):  # func => addition
    def inner_func(*args, **kwargs):
        pw = input("Enter your password ")
        if pw == '123':
            return func(*args, **kwargs)
        else:
            return "Invalid Password"
    return inner_func


# @login_required
def addition(a, b):
    return a + b


addition = login_required(addition)  # login required called which returns inner_fxn
result = addition(2, 3)
print(result)


# def a():
#     def b():
#         a = 1
#         b = 2
#         print(a + b)
#         pass
#     return b
#
# a()


@login_required
def sum_of_5(a, b, c, d, e=5):
    return a + b + c + d + e
