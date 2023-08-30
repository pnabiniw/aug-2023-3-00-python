# Lambda functions are the elegant way of creating one-liner functions in Python
# This function doesn't have name. So, it is also called as Anonymous function
# We do not use lambda functions in the places where the function should be called.
# We use it when we need a reference of the function. For example as a parameter in higher
# order functions like map, reduce and filter

def addition(x, y):
    return x + y

print(addition(2, 3))  # 5


add = lambda x, y: x + y
print(add(2, 3))  # 5


# map()
nums = [1, 2, 3, 4, 5]

# def add_15_to_each(element):
#     return element + 15


result = map(lambda x: x + 15, nums)  # map() returns a map object which is an iterator. But to see the
# actual data, we need to convert it to some other datatype
print(list(result))  # [16, 17, 18, 19, 20]


nums = [1, 2, 3, 4, 5]
result = list(map(lambda element: element ** 2, nums))
print(result)  # [1, 2, 3, 4, 5]


# filter()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)  # [2, 4, 6, 8, 10]


# reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(lambda x, y: x + y, nums)
print(result)  # 55
