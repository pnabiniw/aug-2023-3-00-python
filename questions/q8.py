"""
Use filter() function and lambda to filter the tuples from the list whose elements
sum is greater than 10

"""

data = [(1, 2, 3), (15, 5), (8, 1, 1), (20, 21), (10, 20, 30)]

result = list(filter(lambda x: sum(x) > 10, data))
print(result)  # [(15, 5), (20, 21), (10, 20, 30)]
