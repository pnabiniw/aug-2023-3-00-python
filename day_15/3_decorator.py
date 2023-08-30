# Decorators are the functions in Python which add extra functionality in the existing function
# It is created on the basis of closure concept

def extra_message(func):
    def inner_fxn():
        print("Im learning Python")
        return func()
    return inner_fxn


@extra_message
def message():
    print("Hello World")


# message = extra_message(message)
message()

