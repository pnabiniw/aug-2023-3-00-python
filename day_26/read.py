from orm import session, Student

# reading all data at once
results = session.query(Student).all()  # [obj1, obj2, obj3]  # ORM (Object Relational Mapping)
print(results)
s2 = results[1]
print(s2.name)

for student in results:
    print(student.name)
    print(student.age)


filtered_student = session.query(Student).filter(Student.id == 3)  # [obj3]
for student in filtered_student:
    print(student.name)

