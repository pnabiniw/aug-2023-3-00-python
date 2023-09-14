from orm import Student, session

s1 = Student(1, "Jon", 30, "M")
s2 = Student(2, "Jane", 34, "F")
s3 = Student(3, "Hary", 40, "M")

session.add(s1)
session.add(s2)
session.add(s3)
session.commit()
print("Student Inserted Successfully !!")
