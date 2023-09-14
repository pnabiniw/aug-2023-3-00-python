from orm import session, Student

session.query(Student).filter(Student.id == 3).delete()  # ORM
session.commit()
print("A row has been deleted !!")
