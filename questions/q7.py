"""
1. What is the order of the arguments in functions and methods
a. Keyword Args / Default Args
b. Positional
c. **kwargs
d. *args

2. Explain *args and **kwargs
"""

def addition(*args, **kwargs):
    print(args)

addition(1, 2, 3, 4, a=5, b=6)
