from orm import session, Student

session.query(Student).filter(Student.id == 3).update({"name": "Ken", "age": 50})  # ORM
session.query(Student).filter(Student.name == "Jon").update({"name": "Gita", "age": 12})  # ORM
session.commit()
print("Student Updated Successfully !!")
