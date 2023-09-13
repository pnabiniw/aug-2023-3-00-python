import json

filename = "students.json"


def delete_student():
    student_id = input("Enter the student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
    filtered_student = list(filter(lambda x: x["id"] == student_id, students))
    if filtered_student:
        student = filtered_student[0]
        students.remove(student)
        with open(filename, "w") as fp:
            fp.write(json.dumps(students, indent=2))
    else:
        print("Invalid Student Id!!")
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
