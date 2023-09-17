"""
1. How to swap two variables in python without using a third variable?
2. What will be the output of following code?
"""


names = ["Jon", "Jane", "Eren", "Ragnar", "Arya"]
print(list(enumerate(names)))

# [(0, "Jon"), (1, "Jane")...]

for index, value in enumerate(names):
    print(index)
    print(value)
