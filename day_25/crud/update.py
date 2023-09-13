import json

filename = "students.json"


def update_student():
    student_id = input("Enter the student id ")
    key = input("Enter the info you want to update ")  # name
    value = input(f"Enter the new {key}")  # Ram  (Jon)
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}, {}]
        filtered_student = list(filter(lambda x: x["id"] == student_id, students))
        if filtered_student:
            student = filtered_student[0]  # {}
            student[key] = value
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
        else:
            print("Invalid Student Id!!")
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
