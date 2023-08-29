nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for i in nums:
    if nums.count(i) > 1 and i not in result:
        result.append(i)

print(result)
