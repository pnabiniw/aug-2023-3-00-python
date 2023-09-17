"""
Use reduce() function to calculate the factorial of 5
"""
from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result) # 120
