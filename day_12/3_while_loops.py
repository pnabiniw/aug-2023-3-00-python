# While is another type of loop in python which iterates until the condition after the while statement
# is truthy. The loop stops once the condition becomes falsy
# The condition parameter must be updated from inside the loop. Otherwise, the loop goes in infinite iteration


a = 0
while a <= 10:
    print(a)
    a += 1


# print first 20 even numbers
num = 0
count = 0

while count != 20:
    if num % 2 == 0:
        print(num)
        count += 1
    num += 1


