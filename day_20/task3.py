"""
Create a dictionary student with keys id, name, age, department.
Take a input from the user, which info (id, name, age or department)
he wants to access and print the result. Handle the possible exceptions.

"""

student = {"id": 1, "name": "Jane", "age": 30, "department": "IT"}
try:
    key = input("Enter the info you want to get ")
    result = student[key]   # student["age"]
except KeyError:
    print("Please provide a valid key ")
else:
    print(f"The {key} of the student is {result}")
