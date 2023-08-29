s = "All the occurrences of a specified character in a given string"
char = input("Enter the character you want to omit ")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each   # "ll the occurrences of"

print(result)
