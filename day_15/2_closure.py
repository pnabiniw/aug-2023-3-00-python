# Closure is the concept in the Functional Python which satisfies the following points:
# 1. There must be a function definition inside a function (i.e. Nested Function)
# 2. Inner function must refer to the parameter of the outer function
# 3. Outer function must return the inner function


def closure_fxn(text):
    def inner_fxn():
        print(text)
    return inner_fxn


result = closure_fxn("Hello World")
result()
