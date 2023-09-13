import json

filename = "students.json"


def read_student():
    student_id = input("Enter the student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}, {}]
    filtered_student = list(filter(lambda x: x['id'] == student_id, students))  # [{}]
    if filtered_student:
        student = filtered_student[0]
        print(student)
    else:
        print("Invalid Student Id!!")
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
