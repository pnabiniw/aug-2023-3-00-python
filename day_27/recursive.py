# If a function is called from the definition of the same function then it is called as a
# recursive function

a = 0

def repeat():
    global a
    print(a)
    a += 1
    if a == 10:
        return
    repeat()

repeat()


# Calculate the factorial of 5 in three different ways; normal loop, reduce() and recursive function
# 1 * 2 * 3* 4 * 5

fact = 1
for i in range(1, 6):
    fact = fact * i

print(fact)


from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 5 * factorial(4) = 5 * 24 = 120
# 4 * factorial(3) = 4 * 6 = 24
# 3 * factorial(2) = 3 * 2 = 6
# 2 * factorial(1) = 2 * 1 = 2
# 1 * factorial(0) = 1 * 1 = 1


result = factorial(5)
print(result)  # 120
