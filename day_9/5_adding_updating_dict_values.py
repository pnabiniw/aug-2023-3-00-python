student = {"name": "Jane", "age": 30, "address": "KTM"}
student["roll_no"] = 21
print(student)  # {"name": "Jane", "age": 30, "address": "KTM", "roll_no": 21}

student["name"] = "Jon"
print(student)   # {"name": "Jon", "age": 30, "address": "KTM", "roll_no": 21}

other_info = {"institute": "Broadway", "phone_no": 9890989878}
student.update(other_info)
print(student)
# {"name": "Jon", "age": 30, "address": "KTM", "roll_no": 21, "institute": "Broadway", "phone_no": 9890989878}

student.update(last_name="ABC")
print(student)
