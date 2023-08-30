# Create a decorator which changes the text of the main function to the upper case


def to_upper(func):   # func => message
    def inner_func(*args, **kwargs):  # txt => hello world
        result = func(*args, **kwargs)  # message("hello world")
        return result.upper()
    return inner_func


@to_upper
def message(txt1, txt2):
    return txt1 + txt2

print(message("hello world", "Python"))  # hello world Python



@to_upper
def another_message(txt):
    return txt